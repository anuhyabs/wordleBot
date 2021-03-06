# wordleBot

Wordle is a web based word game that soared in popularity in 2022 and is currently owned and published by New York Times.
The challenge of the game is to guess a five-letter word in six attempts.
Each time guess is made, the player is informed which of the chosen letters are in the target word.
- The color green indicates that the letter is in the right position.
- The color yellow indicates that the letter exists in the target word but is not in the right position.
- The color black/grey indicates that letter does not exist in the target word.
That’s it!

In the project wordleBot, we create a Python package that can find an optimised solution for the given Wordle (optimistically in the first attempt)using the ⬛🟨🟩 tweet distribution.
This is done by simulations of hypothetical games and comparing the feedback received with data from Twitter by ranking a word based on cosine similarity. 
The inspiration for this project is this excellent [Ben Hammer’s Kaggle project](https://www.kaggle.com/benhamner/wordle-1-6).

### Installing the Package:

1. Clone the repository: ```git clone https://github.com/anuhyabs/wordleBot.git```
2. ```cd wordleBot```
3. ```python setup.py install```

### Example

An example is provided to demonstrate how this library can be used to run the solveWordle for a classic Wordle game. The following command will run this example:
```bash 
python Examples\solveWordle.py
```

### User Profile
- Word Game enthusiasts
- Developers

### Data sources
- https://www.kaggle.com/rtatman/english-word-frequency <br>	
This dataset contains the counts of the 333,333 most commonly-used single words on the English language web, as derived from the Google Web Trillion Word Corpus.
- Twitter data collected using the Twitter API for a specific Wordle ID.

### Use cases
1. Word Game enthusiasts setup the package and run the program to solve the wordle in one guess.
2. Developers who want to build a Wordle Solver using the distribution of tweets for the Wordle ID.

### Package Structure:

```bash
wordleBot
├── Documents
│   ├── FinalPresentation.pdf
│   ├── design_doc.md
│   └── functional_specs.md
├── Examples
│   ├── data
│   │   ├── answers.csv
│   │   └── unigram_freq.csv
│   ├── dataSetup.py
│   └── wordleSimulation.py
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
    ├── test_wordleSimulation.py
    ├── twitterKeys.py
    └── wordleSimulation.py
 ```
