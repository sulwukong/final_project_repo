# pair programming practice

import os
import random

word_bank = ["flexible", "paralyzed", "summit", "profession", "challenge", "entertain", 
             "proclaim", "greeting", "justice", "classify", "button", "appeal", "settlement", "salad",
             "character", "land", "total"]


word = random.choice(word_bank)
print(word)
guess_count = 0
score = 0
remaining_tries = 3

while guess_count < 3:

    guess = str(input("Guess a letter or word:  \n"))

    length = len(guess.strip())
    guess_short = guess.strip()

    if length == 1:
        count = word.count(guess)
        score += 1
        print(f"The letter '{guess}' appeared {count} times in the word. Your score is {score}.")


    elif length > 1:
        if guess_short == word:
            print(f"Correct! The word was {guess_short}.")
            break
        else:
            guess_count += 1
            remaining_tries = 3 - guess_count
            print(f"{guess_short} is not the word. You have {remaining_tries} attempts left.")

