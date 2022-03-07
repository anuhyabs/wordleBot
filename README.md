# wordleBot

Wordle is a web based word game that soared in popularity in 2022 and is currently owned and published by New York Times.
The challenge of the game is to guess a five-letter word in six attempts.
Each time guess is made, the player is informed which of the chosen letters are in the target word.
The color green indicates that the letter is in the right position.
The color yellow indicates that the letter exists in the target word but is not in the right position.
The color black/grey indicates that letter does not exist in the target word.
That’s it!

In the project wordleBot, we create a Python package that can find an optimised solution for the given Wordle (optimistically in the first attempt).

### Installing the Package:
```bash
python setup.py install
```
### Package Structure:

```bash
.
├── Documents
├── Examples
│   └── example.py
├── LICENSE
├── README.md
├── setup.py
└── wordleBot
    ├── __init__.py
    ├── data
    │   ├── possible_words.csv
    │   ├── tweets.csv
    │   └── unigram_freq.csv
    ├── dataSetup.py
    ├── getTweets.py
    ├── solveWordle.py
    ├── tests
    │   ├── test_getTweets.py
    │   ├── test_solveWordle.py
    │   └── test_wordleSimulation.py
    ├── twitterKeys.py
    └── wordleSimulation.py
 ```

