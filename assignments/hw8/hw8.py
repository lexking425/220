"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math
from graphics import *

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in nums:
        acc += i
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])


def sum_of_square(nums):
    for i in nums:
        list1 = i.split()
        to_numbers(list1)
        square_each(list1)
        print("sum of squares = " + str(sum_list(list1)))

# tells you if you are going to start or not according to your weight and amount of wins
def starter():
    weight = eval(input("enter weight: "))
    wins = eval(input("enter the amount of wins: "))
    if 150 <= weight < 160 and wins >= 5:
        print("This player will be able to start!")
    if 199 <= weight or wins >= 20:
        print("This player will be able to start!")
    else:
        print("This player will not be able to start.")


# this code tells you if the year you input is a leap year or not
def leap_year():
    year = eval(input("input a year: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# this code tells you if the circles overlap or not
def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("green")
    circle_two.draw(win)

    if math.sqrt(((center2.getX() - center.getX()) ** 2) + ((center2.getY() - center.getY()) ** 2)) < radius + radius2:
        inst_pt = Point(350, 500)
        instructions = Text(inst_pt, "The circles are overlapping!")
        instructions.draw(win)
        print("The circles are overlapping!")
    else:
        inst_pt2 = Point(350, 500)
        instructions2 = Text(inst_pt2, "The circles are not overlapping!")
        instructions2.draw(win)
        print("The circles are not overlapping!")
    close_pt = Point(350, 600)
    close = Text(close_pt, "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    pass
# i wrote all the code for this in the one above


if __name__ == '__main__':
    pass
