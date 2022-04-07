'''
Lex King
lab11.py
this code uses the secret door from last lab to play a game
this is my code
'''
from random import choice
from graphics import Rectangle, GraphWin, Point, Text
from lab10.button import Button
from lab10.door import Door

def door_clicked(click, door1, door2, door3):
    chosen_door = ""
    if door1.is_clicked(click) is True:
        chosen_door = door1
    elif door2.is_clicked(click) is True:
        chosen_door = door2
    elif door3.is_clicked(click) is True:
        chosen_door = door3
    return chosen_door

def three_door_game():

    win = GraphWin("Three Door Game", 400, 400)

    start = Text(Point(200, 75), "I have a secret door")
    start2 = Text(Point(200, 375), "Click to guess which is the secret door!")
    start.draw(win)
    start2.draw(win)

    quit_button = Rectangle(Point(300, 25), Point(350, 50))
    door1 = Rectangle(Point(25, 100), Point(125, 300))
    door2 = Rectangle(Point(150, 100), Point(250, 300))
    door3 = Rectangle(Point(275, 100), Point(375, 300))
    quit = Button(quit_button, "Quit")
    quit.draw(win)

    door1_draw = Door(door1, "Door 1")
    door1_draw.draw(win)
    door2_draw = Door(door2, "Door 2")
    door2_draw.draw(win)
    door3_draw = Door(door3, "Door 3")
    door3_draw.draw(win)

    door_list = [door1, door2, door3]
    secret_door = choice(door_list)
    winner_text = Text(Point(200, 75), "You Win!")
    loser_text = Text(Point(200, 75), "Sorry, Incorrect!")
    again_text = Text(Point(200, 375), "Click anywhere to play again")

    while (door1.is_clicked() or door2.is_clicked() or door3.is_clicked()) is False:
        win.getMouse()

    if chosen_door(door1, door2, door3) == secret_door:
        chosen_door(door1, door2, door3).color_door("green")
        start.undraw()
        start2.undraw()
        winner_text.draw(win)
        again_text.draw(win)
    else:
        chosen_door(door1, door2, door3).color_door("red")
        start.undraw()
        start2.undraw()
        loser_text.draw(win)
        again_text.draw(win)

    win.getMouse()
    win.close()
