"""
Lex King
hw3.py
computing average, total tips, writing a sequence and outputting the approximation of pi.
this is my code
"""


def average():
    grades = eval(input("How many grades will you enter? "))
    add = 0
    total = 0
    for i in range(grades):
        enter_grades = eval(input("Enter Grade: "))
        add = add + enter_grades
    total = add / grades
    print("average is:", total)


def tip_jar():
    sum = 0
    for i in range(5):
        donate = eval(input("how much would you like to donate?"))
        sum = sum + donate
    print("total tips: ", sum)


def newton():
    number = eval(input("What number do you want to square root?"))
    approx = eval(input("How many times should we improve the approximation? "))
    approx = (approx + number / approx) / 2
    print("the square root is approximately", approx)


def sequence():
    amount = eval(input("how many terms would you like? "))
    terms = 1
    for i in range(amount):
        terms = terms + i % 2 * 2
        print(terms, end='\t')


def pi():
    terms = eval(input("Enter the number of terms in the series: "))
    pi = 1
    total = 1
    for i in range(terms):
        pi = pi + i % 2 * 2
        y = (i + 1) / 2 + (i + 1)
        total = total * (y / pi)
    print(total * 2)


if __name__ == '__main__':
    pass
