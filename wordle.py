"""
The game should ask the user for their initial guess 

The game should only allow 5 letter words to be entered 

The game should check the user?s guess against the correct word 

The game should indicate which letters are in the word in blue 

The game should indicate which letters are in the correct place 

The game should indicate when the user has guessed the correct word 

If the user has not guessed the word in 6 goes they should be told they have not completed the game and told the correct word 
"""

import random
import requests
import colorama
from colorama import Fore
import nltk
from nltk.corpus import words

colorama.init(autoreset=True)
nltk.download('words')
word_list = set(words.words())
words_already_tried = []

def user_input():
    while True:
        x = input("enter your 5 letter guess(all letters only): ").strip().lower()
        if len(x) != 5:
            print("your guess contains more than 5 characters")
            continue
        if not x.isalpha():
            print("your guess contains a non-alphabetic character")
            continue
        if x not in word_list:
            print("your guess is not an actual english word")
            continue
        if x in words_already_tried:
            print("you have already tried this word")
            continue
        words_already_tried.append(x)
        return x

def get_random_word():
    five_letter_words = [word for word in word_list if len(word) == 5 and word.isalpha()]
    return random.choice(five_letter_words)

def print_color(letter, col):
    if col == "g":
        print(Fore.GREEN + letter, end="")
    elif col == "y":
        print(Fore.YELLOW + letter, end="")
    elif col == "r":
        print(Fore.RED + letter, end="")
"""
def check_what_contains_check_whatis(guess, answer):
    guess = guess.lower()
    answer = answer.lower()
    for i in range(5):
        if guess[i] == answer[i]:
            print_color(guess[i], "g")
        elif guess[i] in answer:
            print_color(guess[i], "y")
        else:
            print_color(guess[i], "r")
"""
def check_guess(guess, answer):
    guess = guess.lower()
    answer = answer.lower()
    remaining = list(answer)

    # First pass: greens
    colors = [''] * 5
    for i in range(5):
        if guess[i] == answer[i]:
            colors[i] = 'g'
            remaining[i] = None  # remove it so we don't reuse it for yellows

    # Second pass: yellows and reds
    for i in range(5):
        if colors[i] == '':
            if guess[i] in remaining:
                colors[i] = 'y'
                # mark off the first occurrence so that further duplicates won't match
                remaining[remaining.index(guess[i])] = None
            else:
                colors[i] = 'r'

    # Print with colors
    for i in range(5):
        print_color(guess[i], colors[i])
    print()  # newline after the guess

while True:
    print("""
Welcome to Wordle
- Guess the 5-letter word.
- Letters in the correct position will be green.
- Letters in the word but in the wrong position will be yellow.
- Letters not in the word will be red.
- You have 6 attempts.
""")
    answer = get_random_word()
    for i in range(6):
        print("\nno of attempts left:", 6 - i)
        guess = user_input()
        check_what_contains_check_whatis(guess, answer)
        if guess == answer:
            print(f"you have guessed the word '{answer}' correctly")
            break
    else:
        print("\nyou lost, the correct word was:",answer)
    
    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("bye")
        break
    words_already_tried.clear()
