"""
Lex King
hw2.py
I wrote code that calculates the sum of all multiples of 3, made a multiplication table,
calculate the area of a triangle, find the sum of square roots, and finding the power.
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    sum = 0
    for i in range(3, upper_bound + 1, 3):
        sum += i
    print("sum of threes is",sum)

def multiplication_table():
    for row in range(1,11):
        for column in range (1,11):
            print(row * column, end= "\t")
        print('')

def triangle_area():
    length_a = eval(input("Enter side a length: "))
    length_b = eval(input("Enter side b length: "))
    length_c = eval(input("Enter side c length: "))
    s = (length_a + length_b + length_c) / 2
    a = s * (s - length_a) * (s - length_b) * (s - length_c)
    area = math.sqrt(a)
    print("Area is ", area)


def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    middle = upper - 1
    sum = (lower * lower) + (middle * middle) + (upper * upper)
    print(sum)

def power():
    base = int(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    answer = 1
    for i in range(exponent):
        answer = base * answer
    print(base, "^", exponent, "=", answer)

if __name__ == '__main__':
    pass
