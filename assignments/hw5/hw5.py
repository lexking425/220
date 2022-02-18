"""
Lex King
hw5.py
this code prints the names in reverse, company name, initials of names, names the 3rd letter, and finds the pig latin of a sentence.
this is my code
"""


def name_reverse():
    name = input("enter a name(first and last): ")
    name_split = name.split(' ')
    first = name_split[0]
    last = name_split[1]
    print(last + ", " + first)

def company_name():
    domain = input("Enter a domain:")
    company = domain.split(".")
    output = company[1]
    print(output)


def initials():
    students = eval(input("How many students are in the class? "))
    for i in range(students):
        first_name = input("enter the first name of student " + str(i + 1) + ":")
        last_name = input("enter " + first_name + "'s last name:")
        initial = first_name[0] + last_name[0]
        print(initial.capitalize())


def names():
    list = input("Enter a list of names: ")
    split = list.split(",")
    for i in split:
        split = i.split(" ")
        initials = split[0][0] + split[1][0]
        print(initials, end = " ")


def thirds():
    number = eval(input("Enter the number of sentences: "))
    for i in range(number):
        sentence = input("enter sentence " + str(i + 1) + ": ")
        length = len(sentence)
        for j in range(0, length, 3):
            print(sentence[j], end = ' ')
        print('\n')


def word_average():
    sentence = input("enter a sentence: ")
    split = sentence.split(' ')
    acc = 0
    for i in range(len(split)):
        word = split[i]
        acc += len(word)
    average = acc / len(split)
    print(average)


def pig_latin():
    sentence = input("enter sentence: ")
    sentence_lower = sentence.lower()
    words = sentence_lower.split(" ")
    for i in words:
        print(i[1:] + i[0] + "ay", end=" ")



if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
