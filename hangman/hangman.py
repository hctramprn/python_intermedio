# Investigar la función enumerate
# Investigar el método get de los diccionarios
# Investigar la sentencia os.system("clear")
# Mejorar con un sistema de puntos
# Mejorar con código ASCII
# Mejorar la interfaz


# Pseudocode
# Import OS and clear the terminal
# Import words from file
# Choose a random word
# Enumerate the chosen word
# Clear the screen
# Start the game with a given number of lives
# While lives is greater than 0 loop, ask for a letter
# If letter is in dict, display it in the terminal. Else substract a live

import os
import random
from unicodedata import normalize


# import data file and randomly choose a word
def import_data():
    words = []
    with open('./hangman/data.txt', 'r', encoding='utf-8') as data:
        for word in data:
            words.append(word.rstrip().lower())
        hangman_word = random.choice(words)

        # Normalize, encodes and decodes the chosen word to remove any accents
        hangman_word_norm = normalize('NFD', hangman_word)
        hangman_word_encode = hangman_word_norm.encode('ASCII', 'ignore')
        hangman_word_decode = hangman_word_encode.decode('ASCII')

        # Creates a dict enumerating each of the characters in the word
        split_word = dict(enumerate(hangman_word_decode, 0))
        game(split_word)

# clear the terminal
def clear_terminal():
    os.system('clear')

# hangman game
def game(split_word):
    clear_terminal()
    lives = 8
    ok_values = []

    while lives:
        clear_terminal()
        try:
            character = input('Please choose a letter: ').lower()
            if not (character.isalpha() and character.isascii()):
                raise ValueError
        except ValueError:
            input(
                '\nYou must choose a valid letter [A-Z/a-z]. Press Enter to try again...\n')
            continue

        if len(character) != 1:
            input(
                f'\nYou have entered {len(character)} characters. Please only choose ONE letter. Press Enter to try again...\n')
            continue

        print(split_word)
        if character in split_word.values():

            #For loop that appends the index of the correct characters
            # for key in split_word:
            #     if split_word[key] == character:
            #         ok_values.append(key)

            #Lambda function
            # guessed_value = list(filter(lambda key: split_word[key] == character, split_word))
            # ok_values += guessed_value

            #List comprehension
            guessed_value = [key for key in split_word if split_word[key] == character]
            ok_values += guessed_value
            input(ok_values)
        else:
            input('No está')


def run():
    import_data()


if __name__ == '__main__':
    run()
