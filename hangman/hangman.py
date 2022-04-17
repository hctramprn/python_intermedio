import os
import random
from unicodedata import normalize
from hangman_art import HANGMAN_ART

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
        game(hangman_word_decode)

# clear the terminal
def clear_terminal():
    os.system('clear')

# hangman game
def game(hangman_word_decode):
    # Creates a dict enumerating each of the characters in the word
    split_word = dict(enumerate(hangman_word_decode, 0))

    #Set the initial conditions for the game
    clear_terminal()
    lives = 6
    ok_values = []
    chosen_characters = []
    hidden_word = ' _ ' * len(split_word)

    # Runs the game until lives is greater than 0
    while lives:
        clear_terminal()
        hangman_ascii = HANGMAN_ART[6 - lives]

        # Ask for a string of one valid character [A-Z/a-z]
        try:
            character = input(
                f'Lives: {lives}\n\n{hangman_ascii}\n\n{hidden_word}\n\nPlease choose a letter: ').lower()
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

        # Checks if it is a new character
        if (character in chosen_characters):
            input(
                f'\nThis character has already been chosen. Press Enter to try again...\n')
            continue
        else:
            chosen_characters.append(character)

        #Checks if the character is in the dict
        if character in split_word.values():

            # For loop that appends to a list the index of the correct characters
            # for key in split_word:
            #     if split_word[key] == character:
            #         ok_values.append(key)

            # Lambda function
            # guessed_value = list(filter(lambda key: split_word[key] == character, split_word))
            # ok_values += guessed_value

            # List comprehension adds the charater to an ok_values list for future validation
            guessed_value = [
                key for key in split_word if split_word[key] == character]
            ok_values += guessed_value
        else:
            #substracts 1 and checks if there are more lives left
            input(
                '\nThe chosen letter is not in the word ☹️. \n\nPress Enter to try again...\n')
            lives -= 1
            if lives == 0:
                clear_terminal()
                play_again = input(
                f'{HANGMAN_ART[6]} \n\nYou are out of lives ☹️. The word was: \n\n{hangman_word_decode}\n\nDo you want to play again? (Y/N)').lower()
                if play_again == 'y' or play_again == 'yes':
                    run()
            continue

        #prints the respective ascii art for the lives left and the chosen word progress
        hidden_word = ''
        for char in split_word:
            if char in ok_values:
                hidden_word += ' ' + split_word[char] + ' '
            else:
                hidden_word += ' _ '

        #checks if there are more characters left to guess; ends the game
        if len(split_word) == len(ok_values):
            clear_terminal()
            play_again = input(
                f'Congratulations! You guessed the word: \n\n{hangman_word_decode} \n\nDo you want to play again? (Y/N)').lower()
            if play_again == 'y' or play_again == 'yes':
                run()
            else:
                break


def run():
    import_data()


if __name__ == '__main__':
    run()