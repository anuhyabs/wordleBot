#setup.py
from setuptools import setup, find_packages

setup(
    name='wordleBot',
    version='0.0.1',
    description='Python package to train a bot to find an optimised solution for a given Wordle.',
    author='Anuhya Bhagavatula, Shrusti Ghela, Anagha Bandaru',
    author_email='anuhyabs@uw.edu, sghela@uw.edu, anaghadb@uw.edu',
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='python, wordle',
    packages=find_packages(),
    install_requires=['pandas','scipy','pickle','itertools','Counter','tweepy','pytz','datetime','re'],
)

