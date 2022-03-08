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
The dataSetup class is used to set up the data set of all possible answers and their frequency. In this class there are three functions. 
| DataSetup              |
|------------------------|
| getData()              |
| cleanData(data)        |
| addWordleAns(new_data) |


#### GetTweets
The getTweets is a custom class that is used to pull a sample of tweets (5000) of a given Wordle id, filters those tweets that are valid, and adds it to the tweets.csv dataset.
| GetTweets              |
|------------------------|
| twitterAuth()          |
| getWordleID()        |
| is_valid_wordle_tweet(tweet, wordle_id) |
| pullTweets(self,api,wordle_id) |

#### WordleSimulation
After the dataset was cleaned and ready to use, another custom class created - wordleSimulation, that is used to simulate the wordle game for all the possible answers - the words in the dataset that we created using the dataSetup class. 
| WordleSimulation              |
|------------------------|
| __init__(self) |
| evaluate_guess_char(answer, guess, pos) |
| evaluate_guess(self,answer, guess) |
| simulate_wordle(self,answer,starting_weights) |
| run_simulations(self,word, num_sims) |
| getSimRes(self,sim_results) |
| main(self) |

#### SolveWordle




