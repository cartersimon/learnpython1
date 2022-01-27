import random
from words import words
import string
from os import system

def get_valid_word(words):
    while True:
        word = random.choice(words)    
        if '-' in word or ' ' in word:
            continue
        else:
            break
    return word.upper()



def hangman():
    def clear():
        _ = system('cls')

    word = get_valid_word(words)
    word_letters =set(word) # set containing the letters of chosen word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # letters the user has guessed

    lives = 6

    # get user input
    while len(word_letters) > 0 and lives > 0:
        clear()
        # letters used
        # join creates a string from the elements of used_letters
        # using a space as the separator between elements
        if len(used_letters) == 0:
            print('\nWelcome to Hangman! \nYou have', lives, 'lives.')
        else:
            print('\nLives:', lives, '\nUsed letters: ', ' '.join(sorted(used_letters)))
        # added the sorted() function to sort the set in place, returns a list

        # show current state of word with dashes for unknown letters
        ###*** Look up this syntax for an explaination of how it works ***###
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Type a letter to guess: ').upper()
        if user_letter in alphabet - used_letters:
            # if guess is in alphabet and wasn't already guessed
            used_letters.add(user_letter)
            if user_letter in word_letters:
                # if guess is in word remove it from word_letters
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('That letter was not in the word.')
        elif user_letter in used_letters:
            print('You already guessed that letter, try another.')
        else:
            print('You entered an invalid character. Try again.')
    
    # gets here when len(word_letters) == 0 i.e. they successfully guessed word
    # OR they're here because they ran out of lives
    if lives == 0:
        print('Sorry, you ran out of lives. The word was: ', word)
    else:
        print('You correctly guessed the word:', word, '\n')

while True:
    hangman()
    ip = input('Enter \'Y\' to play again, anything else to quit:').upper()
    if ip != 'Y':
        break