# wordleBot

Wordle is a web based word game that soared in popularity in 2022 and is currently owned and published by New York Times.
The challenge of the game is to guess a five-letter word in six attempts.
Each time guess is made, the player is informed which of the chosen letters are in the target word.
The color green indicates that the letter is in the right position.
The color yellow indicates that the letter exists in the target word but is not in the right position.
The color black/grey indicates that letter does not exist in the target word.
That’s it!

In the project wordleBot, we create a Python package that can find an optimised solution for the given Wordle (optimistically in the first attempt).

### File Structure/Architecture:

wordleBot
├── LICENSE
├── README.md
├── Documents
├── Examples
├── wordleBot
│   ├── __init__.py
│   ├── data
│   │	├── google words
│   │	├── unigram_freq.csv
│   │	├── possible_words.csv	
│   │	├── frequency.csv
│   │	├── tweets.csv
│   ├── tests
│   │	├── test_wordleSimulation.py
│   │	├── test_getTweets.py
│   │	├── test_solveWordle.py
│   ├── wordleSimulation.py
│   ├── solveWordle.py
│   ├── dataSetup.py
│   ├── getTweets.py
└── setup.py

