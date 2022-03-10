#solveWordle.py
"""
Created on Sun Mar  6 17:12:02 2022
Name: Solve Wordle
Description: Assign ranking to words to make the correct first guess to solve Wordle
"""
import pandas as pd
import pickle
from GetTweets import GetTweets
import Counter
from itertools import product
from scipy import spatial
import re

class SolveWordle:
    
    def __init__(self):
	'''
	Contructor that declares all the class variables of solveWordle.
	'''
        self.v_all = None
        self.v_ratio = None
        self.invalid_results = None
        self.tweet_data = None
        self.words = None
        self.words_ind = None
        self.vec_locs = sorted(["".join(x) for x in product("YMN", repeat=5)])
        
    def importData(self):
    	'''
	Import data from files  that were the outputs for WordleSimulation, getTweets and dataSetUp.
	'''
        with open("./data/vec_all.pickle", "rb") as f:
            self.v_all = pickle.load(f)
    
        with open("./data/vec_ratio.pickle", "rb") as f:
            self.v_ratio = pickle.load(f)
        
        with open("./data/invalid_results.pickle", "rb") as f:
            self.invalid_results = pickle.load(f)
            
        tweets = GetTweets()
        tweets.getTweets()
        self.tweet_data = pd.read_csv("./data/tweets.csv")
        self.words = pd.read_csv("./data/possible_words.csv")
        self.words_ind = self.words.iloc[:,0]
    
    def wordle_guesses(tweet):
        '''
	Replace the green/yellow/black/grey tiles in the guesses with 'Y','M','N'.
	Input: String that contains the tweet data from all the tweets collected.
	'''
	text = (tweet.replace("Y", "y").replace("🟩", "Y")
                     .replace("M", "m").replace("🟨", "M")
                     .replace("N", "n").replace("⬛", "N").replace("⬜", "N"))
        guesses = re.findall("([YMN]+)", text)
        return guesses


    def computeRank(self):
	'''
	Computes the rank of the words based on the distribution obtained from tweets and pre computed simulations.
	Prints the output of the game.
	'''
        results = []
    
        for i in sorted(set(self.tweet_data["wordle_id"])):
            tweet_texts = self.tweet_data[self.tweet_data["wordle_id"]==i]["tweet_text"]
        
        games = [self.wordle_guesses(tweet) for tweet in tweet_texts]   
        
        all_counts = Counter(res for game in games for res in game if len(game)>=2 and game[-1]=="YYYYY")
        first_counts = Counter(game[0] for game in games if len(game)>=2 and game[-1]=="YYYYY")
        penultimate_counts = Counter(game[-2] for game in games if len(game)>=2 and game[-1]=="YYYYY")
        
        self.vec_all = [all_counts[res] for res in self.vec_locs]
        self.vec_first = [first_counts[res] for res in self.vec_locs]
        self.vec_penultimate = [penultimate_counts[res] for res in self.vec_locs]
        self.vec_ratio = [penultimate_counts[res]/(all_counts[res]+1e-6) for res in self.vec_locs]
        
        dists = {"all": [], "ratio": []}
        
        for key in self.v_all:
            dists["all"].append((spatial.distance.cosine(self.vec_all, self.v_all[key]), key))
            dists["ratio"].append((spatial.distance.cosine(self.vec_ratio, self.v_ratio[key]), key))
        
        dists["invalid"] = [(len([g for g in games if any(r in self.invalid_results[key] for r in g)]), key) for key in self.v_all]
    
        ranks = {}
        for d in dists:
            s = sorted(dists[d])
            ranks[d] = {s[i][1]: i for i in range(len(s))}
        
        overall = []
        for key in self.v_all:
            overall.append((sum(ranks[r][key] for r in ranks), key))
        
        my_guess = sorted(overall)[0][1]
        answer = self.words_ind[i]
        answer_rank = [x[1] for x in sorted(overall)].index(answer)
            
        results.append([i, my_guess, answer, answer_rank, overall, dists, ranks])
        feedback = self.evaluate_guess(answer, my_guess).replace("Y", "🟩").replace("M", "🟨").replace("N", "⬛")
    
        if answer==my_guess:
            feedback += " !!!!!!"
        else:
            feedback += " the actual answer ranked %d on my guess list" % (answer_rank)
            
        if i<max(self.tweet_data["wordle_id"]):
            print("For Wordle %d, my guess was %s. %s" % (i, my_guess, feedback))
        else:
            print("For today's Wordle %d, my result was: %s" % (i, feedback))
    
def main():
    solveWordle = SolveWordle()    
    solveWordle.importData()
    solveWordle.computeRank()
    
    
if __name__ == "__main__":
    main()
