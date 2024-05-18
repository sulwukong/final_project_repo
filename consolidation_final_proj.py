# Word Guessing Game

import os
import random
import matplotlib.pyplot as plt

score_file = "score_file.txt"
scores = {}
if os.path.exists(score_file):
    with open(score_file, "r") as file:
        for line in file:
            name, score = line.strip().split(":")
            scores[name] = int(score)

word_bank = ["flexible", "paralyzed", "summit", "profession", "challenge", "entertain", 
             "proclaim", "greeting", "justice", "classify", "button", "appeal", "settlement", "salad",
             "character", "land", "total", "plaintiff", "leadership", "guest", "obligation", "cooperative", "summary",
             "demonstration", "graphic"]


word = random.choice(word_bank)
# print(word)
wordlength = len(word)
guess_count = 0
score = 0
remaining_tries = 3

print(f"The word is {wordlength} characters long.")

while guess_count < 3:

    guess = str(input("Guess a letter or word:  \n"))

    length = len(guess.strip())
    guess_short = guess.strip()

    if length == 1:
        count = word.count(guess_short)
        score += 1
        print(f"The letter '{guess_short}' appeared {count} times in the word. Your score is {score}.")


    elif length > 1:
        if guess_short == word:
            print(f"Correct! The word was {guess_short}.")
            break
        else:
            guess_count += 1
            remaining_tries = 3 - guess_count
            print(f"{guess_short} is not the word. You have {remaining_tries} attempts left.")

print(f"Your score was {score}")

player_name = input("Enter your name to save your score: ").strip()
scores[player_name] = score
with open(score_file, "w") as file:
    for name, score in scores.items():
        file.write(f"{name}:{score}\n")

names = list(scores.keys())
scores_list = list(scores.values())
plt.bar(names, scores_list)
plt.xlabel('Player')
plt.ylabel('Score')
plt.title('Word Guessing Game Score Graph')
plt.ylim(0,10)
plt.show()