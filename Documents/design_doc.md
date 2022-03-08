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
The inspiration for this project is this excellent Ben Hammer’s Kaggle project.

## Design Overview

The project consists of four main components : DataSetup, GetTweets, WordleSimulation, SolveWordle.

### Design details

#### DataSetup
#### GetTweets
#### WordleSimulation
#### SolveWordle




