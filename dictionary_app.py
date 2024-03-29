# dictionary_app.py
# David Kislyak
# 3/15/2018
# CLI dictionary application

from difflib import get_close_matches
from json import load

data = load(open("data.json"))  # secretly is: open("data.json", "r")

def word_lookup(word):
    #__init__
    #close_matches = []
    word = word.lower()

    # Attempt to look for the user input in the dictionary 
    try:
        definition_list = data[word]

    # If that fails and raises a KeyError:
    except KeyError:

        # Attempt to find similar words to the users word
        close_matches = get_close_matches(user_input, data.keys())

        # If there any close matches:
        if len(close_matches) > 0:
            print("\nDid you mean: ")

            # For every close match found:
            num = 1
            for word in close_matches:
                print(f'{num}.) {word.capitalize()}')
                num += 1
            print("0.) My word is not on here")

            # Gather user input about word selection and subtract one to index properly
            user_correct_word = int(input("\nWhat is your word: ")) - 1

            # If user selected an option that is not available
            if user_correct_word <= -2 or user_correct_word > len(close_matches) - 1:
                raise ValueError("Sorry, that doesn't seem like an option.")

            # If user selects that their word is not on the list:
            elif user_correct_word == -1:
                raise ValueError("Sorry I guess I can't find that word.")

            # If the user has picked a word from the list:
            elif user_correct_word <= len(close_matches) - 1:
                return data[close_matches[user_correct_word]]

        else:
            # There are no close_matches:
            raise ValueError("I can't find that word. Please double check the word.")
            
    return definition_list


# Ask user for input and save to variable: user_input
user_input = input("What word would you like to look up the definition for: ")

# Call function word_lookup and save response to variable: definition
try:
    definitions = word_lookup(user_input)

    # for each different definition returned:
    for definition in definitions:
        print(f'{definition}\n')
except ValueError as error:
    print(error)

# Keep program from automatically closing
input()
