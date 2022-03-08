#test_wordleSimulation.py
"""
Created on Tue Mar  1 17:57:45 2022
Name: test_wordleSimulation
Description : Tests whether the guess is being evaluated correctly with the answer
"""
from wordleBot.WordleSimulation import WordleSimulation

obj = WordleSimulation()
def test_sim():
    assert obj._evaluate_guess("tools", "break")=="NNNNN"
    assert obj._evaluate_guess("tools", "tools")=="YYYYY"
    assert obj._evaluate_guess("tools", "tolls")=="YYNYY"
    assert obj._evaluate_guess("tools", "books")=="NYYNY"
    assert obj._evaluate_guess("tools", "broke")=="NNYNN"
    assert obj._evaluate_guess("tools", "yahoo")=="NNNMM"
    assert obj._evaluate_guess("tools", "bongo")=="NYNNM"
    assert obj._evaluate_guess("tools", "brook")=="NNYMN"
    assert obj._evaluate_guess("rates", "ranks")=="YYNNY"
    assert obj._evaluate_guess("rates", "apple")=="MNNNM"
    
if __name__ == "__main__":
    test_sim()