import requests 
from termcolor import colored

word = "flame"
guess = "asdf"
guesses = 6

while True:
    print(f"You have {guesses} guesses left")
    guess = input()
    while len(guess) != 5 or type(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + guess).json()) == dict:
        print("That is not a valid guess. Try again.")
        guess = input()
    
    output = []
    for i in range(len(guess)):
        if guess[i] == word[i]:
            output.append(colored(guess[i], "green"))
        elif guess[i] in word:
            output.append(colored(guess[i], "yellow"))
        else:
            output.append(colored(guess[i], "white"))
    print("".join(output))

    if guess == word:
        print("You got the word!")
        break

    guesses -= 1
    if guesses < 1:
        print("You did not get the word :(")
        break