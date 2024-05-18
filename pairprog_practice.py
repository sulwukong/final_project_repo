# pair programming practice

import os
import random

word_bank = ["flexible", "paralyzed", "summit", "profession", "challenge", "entertain", 
             "proclaim", "greeting", "justice", "classify", "button", "appeal", "settlement", "salad",
             "character", "land", "total"]

word = random.choice(word_bank)
print(word)
guess = str(input("Guess a letter:  \n"))

length = len(guess.strip())
guess_short = guess.strip()

if length == 1:
    count = word.count(guess)
    print(f"The letter '{guess}' appeared {count} times in the word.")
elif length > 1:
    if guess_short == word:
        print(f"Correct! The word was {guess_short}.")
    else:
        print(f"{guess_short} is not the word.")

