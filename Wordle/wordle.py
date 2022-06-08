import requests 
import random
import os
from termcolor import colored

path = os.path.dirname(__file__) + "/wordlist.txt"
f = open(path, "r").readlines()
word = random.choice(f)[0:5]
open(path, "r").close()
wordindices = {}
guess = "asdf"
guesses = 6
guessed = []

for i in range(5):
    if word[i] not in wordindices:
        wordindices.update({word[i]: [i]})
    else:
        wordindices[word[i]].append(i)

while True:
    guess = input(f"You have {guesses} guesses left: ")
    while len(guess) != 5 or type(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + guess).json()) == dict:
        guess = input("That is not a valid guess. Try again: ")
    
    guessindices = {}
    for i in range(5):
        if guess[i] not in guessindices:
            guessindices.update({guess[i]: [i]})
        else:
            guessindices[guess[i]].append(i)

    output = []
    for i in range(5):
        if guess[i] not in word:
            output.append(colored(guess[i], "white"))
        else:
            a = wordindices[guess[i]]
            b = guessindices[guess[i]]
            matching = set(a) & set(b)

            if i in matching:
                output.append(colored(guess[i], "green"))
            elif len(a) == len(b):
                output.append(colored(guess[i], "yellow"))
            else:
                if len(a) - len(matching) == 0:
                    output.append(colored(guess[i], "white"))
                elif len(a) < len(b) and b.index(i) >= len(b) - len(a) - len(matching):
                    output.append(colored(guess[i], "white"))
                else:
                    output.append(colored(guess[i], "yellow"))

    guessed.append("".join(output))
    print("\n".join(guessed))

    if guess == word:
        print("You got the word!")
        break

    guesses -= 1
    if guesses < 1:
        print("You did not get the word :(")
        print(f"The word was {word}")
        break