# wordleSimulation.py
"""
Created on Sat Mar  5 17:43:06 2022
Name: Wordle Simulation
Description: Simulate Wordle game for all possible answers
"""

import numpy as np
import pandas as pd
import ray
import gc
import Counter
from itertools import product
import pickle

class WordleSimulation:

    def __init__(self):
    	'''
        Constructor to initialize variables for the class.
        '''
        self.words = pd.read_csv('./data/possible_words.csv',header = 0)
        self.vec_locs = sorted(["".join(x) for x in product("YMN", repeat=5)])
        self.words_array = np.zeros((5, len(self.words)))
        self.words_ind = self.words.iloc[:,0]
        for i in range(len(self.words_ind)):
            for loc in range(5):
                self.words_array[loc, i] = ord(self.words_ind[i][loc])

    def _evaluate_guess_char(answer, guess, pos):
        '''
        Compares the character in guess with characters in answer.

        Parameters
        ----------
        answer : String
            The final value of the game.
        guess : String
            Each guess made to reach the answer.
        pos : Number
            Position of character to compare.

        Returns
        -------
        'Y','M' or 'N' - indication about the characters in guess word.
        '''
	if answer[pos]==guess[pos]:
            return "Y"
        unmatched_answer_chars = 0
        unmatched_guess_chars = 0
        this_guess_num = 0
        for i in range(5):
            if answer[i]==guess[pos]:
                if answer[i]!=guess[i]:
                    unmatched_answer_chars += 1
            if guess[i]==guess[pos]:
                if answer[i]!=guess[i]:
                    unmatched_guess_chars += 1
                    if i<pos:
                        this_guess_num += 1
        if this_guess_num<unmatched_answer_chars:
            return "M"
        return "N"

    def _evaluate_guess(self,answer, guess):
        '''
        Calls the _evaluate_guess_char for each character in the guess word
        Parameters
        ----------
        answer : String
            The final value of the game.
        guess : String
            Each guess made to reach the answer.

        Returns
        -------
        Concatenation of 'Y','M','N' for each guess.
        '''
	return "".join(self._evaluate_guess_char(answer, guess, i) for i in range(5)) 

    def _simulate_wordle(self,answer,starting_weights):
       '''
        Randomly selects a word for the first guess and passes the guess word to _evaluate_guess.
        Updates the weights of the words based on the distribution that is returned from _evaluate_guess.

        Parameters
        ----------
        answer : String
            The final value of the game.
        starting_weights : String
            Each guess made to reach the answer.

        Returns
        -------
        game : array
            Returns all possible distributions for a word.
        '''
	weights = self.words.copy()
        game = []
        for i in range(6):
            cum_weights = np.cumsum(weights)
            guess = self.words[np.nonzero(np.random.randint(cum_weights[-1])<cum_weights)[0][0]]
            res = self._evaluate_guess(answer, guess)
            game.append(res)
            if res=="YYYYY":
                break
            for loc in range(5):
                if res[loc]=="Y":
                    weights *= (self.words_array[loc,:]==ord(guess[loc]))
                if res[loc]=="M":
                    locs = [j for j in range(5) if j!=loc]
                    weights *= np.sum(self.words_array[locs,:]==ord(guess[loc]), axis=0)
                if (res[loc]=="N") and (guess[loc] not in [guess[i] for i in range(5) if res[i]=="M"]):
                    for loc2 in range(5):
                        if res[loc2]!="Y":
                            weights *= (self.words_array[loc2,:]!=ord(guess[loc]))
        return game

    @ray.remote
    def _run_simulations(self,word, num_sims):
         '''
        Runns the simulation for a word num_sims times by calling the _simulate_wordle method.

        Parameters
        ----------
        word : String
            A word from the all possible words list.
        num_sims : Number
            The number of times the simulation must be run.

        Returns
        -------
        word : String
        all_counts : array.
        first_counts : array
        penultimate_counts : array
        '''
	games = [self.simulate_wordle(word) for i in range(num_sims)]
        all_counts = Counter(res for game in games for res in game if len(game)>=2 and game[-1]=="YYYYY")
        first_counts = Counter(game[0] for game in games if len(game)>=2 and game[-1]=="YYYYY")
        penultimate_counts = Counter(game[-2] for game in games if len(game)>=2 and game[-1]=="YYYYY")
        return (word, all_counts, first_counts, penultimate_counts)

    def _getSimRes(self,sim_results):
	'''
	Creates dictionaries to store the values of the distributions.
	'''
        sim_vec_all = {}
        sim_vec_ratio = {}
        sim_vec_first = {}
        sim_vec_penultimate = {}

        for (word, all_counts, first_counts, penultimate_counts) in sim_results:
            sim_vec_all[word] = [all_counts[res] for res in self.vec_locs]
            sim_vec_first[word] = [first_counts[res] for res in self.vec_locs]
            sim_vec_penultimate[word] = [penultimate_counts[res] for res in self.vec_locs]
            sim_vec_ratio[word] = [penultimate_counts[res]/(all_counts[res]+1e-6) for res in self.vec_locs]

        self._exportFiles(sim_vec_all,sim_vec_first,sim_vec_penultimate,sim_vec_ratio)
        del sim_results
        gc.collect()

    def _exportFiles(self,sim_vec_all,sim_vec_first,sim_vec_penultimate,sim_vec_ratio):
        '''
	Export files in pickle format
	'''
	with open("./data/vec_all.pickle", "wb") as f:
            pickle.dump(sim_vec_all, f, protocol=pickle.HIGHEST_PROTOCOL)

        with open("./data/vec_first.pickle", "wb") as f:
            pickle.dump(sim_vec_first, f, protocol=pickle.HIGHEST_PROTOCOL)

        with open("./data/vec_penultimate.pickle", "wb") as f:
            pickle.dump(sim_vec_penultimate, f, protocol=pickle.HIGHEST_PROTOCOL)

        with open("./data/vec_ratio.pickle", "wb") as f:
            pickle.dump(sim_vec_ratio, f, protocol=pickle.HIGHEST_PROTOCOL)

    def _invalidRes(self):
	'''
	Remove all invalid vectors in the 'YMN' vectors
	'''
        invalid_results = {}
        for a in self.words:
            invalid_results[a] = set("".join(x) for x in product("YMN", repeat=5))
            for w in self.words:
                r = self._evaluate_guess(a, w)
                if r in invalid_results[a]:
                    invalid_results[a].remove(r)
        with open("./data/invalid_results.pickle", "wb") as f:
            pickle.dump(invalid_results, f, protocol=pickle.HIGHEST_PROTOCOL)

def main():
    '''
    The main functions creates an object of WordleSimulation and calls the functions in it since WordleSimulation is a standalone code
    that can be run once and does not need to be executed again. 
    '''
    ray.init()
    res = []
    num_sims = 10
    for i in range(len(main.words)):
        res.append(main._run_simulations.remote(main.words.iloc[i,0], num_sims))

    sim_results = ray.get(res)
    main._getSimRes(sim_results)
    ray.shutdown()
    gc.collect()

    main._invalidRes()

if __name__ = "__main__":
    main()
