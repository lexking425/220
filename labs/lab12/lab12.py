'''
Lex King
lab12.py
this code finds the first value in the list, inputs a number between 1 and 10, makes sure the number is positive, and hi low game.
this is my code
'''

from random import randint

def find_and_remove_first(list, value):
    list.insert(list.index(value), "Lex")
    list.remove(value)

def good_input():
    value = eval(input("Enter a number between 1 and 10: "))
    while not 1 <= value <= 10:
        value = eval(input("This number is not between 1 and 10! Choose another."))
    return value

def num_digits():
    value = 1
    while value >= 1:
        value = eval(input("enter a positive number: "))
        counts = 0
        val = value
        if val >= 1:
            while val != 0:
                val //= 10
                counts += 1
            print(counts)

def hi_low_game():
    number = randint(1, 100)
    count = 0
    guesses = 0
    while count < 7 and guesses != number:
        guesses = eval(input("Enter your guess: "))
        if guesses > number:
            print("Too High!")
        if guesses < number:
            print("Too Low!")
        if guesses == number:
            print("You are correct!")
        count += 1
    if guesses == number:
        print("You Won! It took you {} guesses!".format(count))
    else:
        print("You lost! The correct number is {}".format(number))



