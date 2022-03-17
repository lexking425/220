'''
Lex King
lab8.py
this code is 2 circles bouncing around in a window and when they hit each other they bounce off each other.
this is my code
'''
from random import randint
from graphics import *
import math

def get_random(move_amount):
    parameter = randint(-move_amount, move_amount)
    return parameter
def did_collide(ball1, ball2):
    ball1_center = ball1.getCenter()
    ball2_center = ball2.getCenter()
    ball1_position_x = ball1_center.getX()
    ball1_position_y = ball1_center.getY()
    ball2_position_x = ball2_center.getX()
    ball2_position_y = ball2_center.getY()

    ball1_radius = ball1.getRadius()
    ball2_radius = ball2.getRadius()

    distance_calc = ((ball2_position_x - ball1_position_x) **2) + ((ball2_position_y - ball1_position_y) **2)
    distance = math.sqrt(distance_calc)
    radius = ball1_radius + ball2_radius

    if distance <= radius:
        return True
    else:
        return False

def hit_vertical(ball, win):
    circle = ball.getCenter().getX()
    if win.height - circle <= ball.getRadius() or abs(0 - circle) <= ball.getRadius():
        return True
    if win.height - circle >= ball.getRadius() or abs(0 - circle) >= ball.getRadius():
        return False
    return None

def hit_horizontal(ball, win):
    circle = ball.getCenter().getY()
    if win.height - circle <= ball.getRadius() or abs(0 - circle) <= ball.getRadius():
        return True
    if win.height - circle >= ball.getRadius() or abs(0 - circle) >= ball.getRadius():
        return False
    return None

def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)

def bumper():
    win = GraphWin("Bumper Cars", 400, 400)
    point1 = Point(200, 200)
    circle1 = Circle(point1, 25)
    circle1.setFill(get_random_color())
    circle1.draw(win)

    point2 = Point(100, 50)
    circle2 = Circle(point2, 25)
    circle2.setFill(get_random_color())
    circle2.draw(win)

    variable_x = get_random(10)
    variable_y = get_random(10)
    variable_x2 = get_random(10)
    variable_y2 = get_random(10)

    while True:
        circle1.move(variable_x, variable_y)
        circle2.move(variable_x2, variable_y2)

        if hit_horizontal(circle1, win) is True:
            variable_y *= -1
            circle1.move(variable_x, variable_y)
        if hit_horizontal(circle2, win) is True:
            variable_y2 *= -1
            circle2.move(variable_x2, variable_y2)

        if hit_vertical(circle1, win) is True:
            variable_x *= -1
            circle1.move(variable_x, variable_y)
        if hit_vertical(circle2, win) is True:
            variable_x2 *= -1
            circle1.move(variable_x2, variable_y2)

        if did_collide(circle1, circle2) is True:
            variable_x *= -1
            variable_x += randint(1, 10)
            variable_y *= -1
            variable_y *= randint(1, 10)
            circle1.move(variable_x, variable_y)

            variable_x2 *= -1
            variable_x2 += randint(1, 10)
            variable_y2 *= -1
            variable_y2 *= randint(1, 10)
            circle2.move(variable_x2, variable_y2)








