'''
lex king
hw9.py
playing hangman
this is my code
'''
from random import choice
from words import words

# gets the word
def get_words(words):
    word = []
    for i in words:
        word.append(i.strip("\n"))
    unknown_word = choice(word)
    return unknown_word


def get_random_word(words):
     random_word = random.choice(words)


def letter_in_secret_word(letter, secret_word):
    pass


def already_guessed(letter, guesses):
    if guesses in letter:
        print("Letter has already been guessed!")
        return True
    else:
        return False

def make_hidden_secret(secret_word, guesses):
    board = []
    for guesses in range(len(secret_word)):
        board.append("_")
    return board


def won(guessed, board):
    return "".join(board) == guessed


def play_graphics(board, guesses):
    print(board)
    print("Wrong Letters: {}".format(guesses))


def play_command_line():
    count = [0]
    guessed = []
    guesses = []
    words = open("words.txt", 'r')
    secret_word = get_words(words)
    board = make_hidden_secret(secret_word)
    while count[0] < 7:
        play_graphics(board, guesses)
        print("\n")
        guesses = input("enter guessed letter: ")
        print("\n")
        already_guessed(letter, guesses)
        if won(guessed, board) is True:
            break
    if won(guessed, board) is True:
        print("Winner!")
    else:
        print("You lost! The word was: {}".format(secret_word))




if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
