"""
Lex King
hw6.py
In this code we convert a number to cash format, encode words, get sphere area and volume, sum of number.
this is my code
"""

# converts a integer to a cash format
def cash_converter():
    integer = eval(input("Enter an integer: "))
    format = "That is ${:.2f}".format(integer)
    print(format)

# encodes a message
def encode():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    # acc = " "
    for i in message:
        number = ord(message[i]) + key
        coded = chr(number)
        print(coded, end=' ')

    #     old_value = ord(message[i]) - 65
    #     shift = ord(key)
    #     new_value = (old_value + shift) % 26
    #     alpha = new_value + 65
    #     final_val = chr(alpha)
    #     acc = acc + final_val
    # print(acc)

# finds the sphere area
def sphere_area():
    radius = eval(input("What is the radius of the sphere? "))
    area = 4 * 3.14 * int(radius) ** 2
    return area

# finds volume of sphere
def sphere_volume():
    radius = eval(input("What is the radius of the sphere? "))
    volume = 4/3 * 3.14 * (int(radius) ** 3)
    return volume


def sum_n(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum


def sum_n_cubes(number):
    sum_cubes = 0
    for i in range(1, number + 1):
        sum_cubes += i ** 3
    return sum_cubes

# this encodes the word dolphin
def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    for i in range(len(message)):
        shift = ord(key[i]) - 97
        coded = chr(ord(message[i]) + shift)
        print(coded, end= " ")


