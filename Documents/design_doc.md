# Design Specification

## Introduction
Wordle is a web based word game that soared in popularity in 2022 and is currently owned and published by New York Times.
The challenge of the game is to guess a five-letter word in six attempts.
Each time a guess is made, the player is informed which of the chosen letters are in the target word.
- The color green indicates that the letter is in the right position.
- The color yellow indicates that the letter exists in the target word but is not in the right position.
- The color black/grey indicates that letter does not exist in the target word.
That’s it!

### Goal
In the project wordleBot, we create a Python package that can find an optimised solution for the given Wordle (optimistically in the first attempt) using the ⬛🟨🟩 tweet distribution.
This is done by precomputing simulations of hypothetical games and comparing the feedback received with data from Twitter by ranking a word based on cosine similarity. 
The inspiration for this project is this excellent [Ben Hammer’s Kaggle project](https://www.kaggle.com/benhamner/wordle-1-6).

## Design Overview

The project consists of four main components : DataSetup, GetTweets, WordleSimulation, SolveWordle.

### Design details

#### DataSetup
The DataSetup class is a stand alone class that is used to set up the data set of all possible answers and their frequency. In this class there are three functions. 

| DataSetup              |
|------------------------|
| \_getData()              |
| \_cleanData(data)        |
| \_addWordleAns(new_data) |

*Input:* Unigram Frequency dataset <br>
*Output:* possible_words.csv

#### GetTweets
The GetTweets is a custom class that is used to pull a sample of tweets (5000) of a given Wordle id, filters those tweets that are valid, and creates a tweets.csv dataset.

| GetTweets              |
|------------------------|
| \_twitterAuth()          |
| \_getWordleID()        |
| \_is_valid_wordle_tweet(tweet, wordle_id) |
| \_pullTweets(self,api,wordle_id) |
| getTweets(self) |

*Output:* tweets.csv

#### WordleSimulation
The WordleSimulation class is used to run simulations of the wordle game for all the possible answers (obtained as the output of DataSetup.py). The frequency distributions for each word are then stored in pickle files and used as inputs to SolveWordle class. This class also acts as a standalone class.

| WordleSimulation              |
|------------------------|
| __init__(self) |
| \_evaluate_guess_char(answer, guess, pos) |
| \_evaluate_guess(self,answer, guess) |
| \_simulate_wordle(self,answer,starting_weights) |
| \_run_simulations(self,word, num_sims) |
| \_getSimRes(self,sim_results) |
| \_exportFiles(self,sim_vec_all,sim_vec_first,sim_vec_penultimate,sim_vec_ratio) |
| \_invalidRes(self) |
| wordleSim(self) |

*Input:* possible_words.csv <br>
*Output:* vec_all.pickle <br>
          vec_first.pickle <br>
          vec_penultimate.pickle <br>
          vec_ratio.pickle <br>
          invalid_results.pickle <br>

#### SolveWordle
The SolveWordle class is used to compute the distribution of Wordle results twitter for a particular id, compare this to the distributions we found from the wordleSimulations class, rank the possible words based on the comparison of the distribution. The word the ranks the highest is our guess for solving the Wordle in the first try!

| SolveWoredle              |
|------------------------|
| __init__(self) |
| importData(self) |
| wordleGuess(Tweet) |
| computeRank(self) |

*Input:* possible_words.csv <br>
         tweets.csv <br>
         vec_all.pickle <br>
         vec_ratio.pickle <br>
         invalid_results.pickle <br>




