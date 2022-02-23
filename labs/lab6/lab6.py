'''
Lex King
lab6.py

this is my code
'''
from graphics import *


def vigenere():
    # creates the window
    win = GraphWin("Vigenere", 500, 500)
    text = Text(Point(100, 100), "Message to code:")
    text2 = Text(Point(100, 150),"Enter Keyword: ")
    text.draw(win)
    text2.draw(win)
    win.setBackground('white')

    message_to_code = Entry(Point(250, 100), 20)
    message_to_code.setFace("times roman")
    keyword = Entry(Point(250, 150), 20)
    keyword.setFace("times roman")
    message_to_code.draw(win)
    keyword.draw(win)

    text3 = Text(Point(250, 225), "Encode")
    p1 = Point(200, 200)
    p2 = Point(300, 250)
    rectangle = Rectangle(p1, p2)
    rectangle.draw(win)
    text3.draw(win)

    win.getMouse()
    message = message_to_code.getText()
    key = keyword.getText()

    # encoding the message
    message = message.replace(" ","")
    message = message.upper()
    key = key.replace(" ","")
    key = key.upper()
    acc = ""
    for i in range(len(message)):
        old_val = ord(message[i]) - 65
        shift = ord(key[i % len(key)]) - 65
        new_val = (old_val + shift) % 26
        alpha = new_val + 65
        final_val = chr(alpha)
        acc = acc + final_val



    # undraws encode message and prints resulting message
    text3.undraw()
    rectangle.undraw()
    text4 = Text(Point(250, 200), "Resulting Message:")
    text4.draw(win)

    result = Text(Point(250, 250), acc)
    result.draw(win)

    close_message = Text(Point(250, 400), "Click Anywhere to Close Window")
    close_message.draw(win)
    win.getMouse()
    win.close()




