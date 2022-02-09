"""

"""
from graphics import GraphWin, Polygon, Point, Text, Circle
from time import sleep
def greeting_card():
    win = GraphWin("Happy Valentine's Day!", 1000, 1000)
    triangle_p1 = Point(250, 150)
    triangle_p2 = Point(750, 150)
    triangle_p3 = Point(500, 750)
    triangle = Polygon(triangle_p1, triangle_p2, triangle_p3)

    left_circle = Circle(Point(380, 150), 125)
    right_circle = Circle(Point(620, 150), 125)

    arrow_head_p1 = Point(100, 250)
    arrow_head_p2 = Point(200, 300)
    arrow_head_p3 = Point(200, 200)
    arrow_head = Polygon(arrow_head_p1, arrow_head_p2, arrow_head_p3)

    arrow_stick_p1 = Point(200, 260)
    arrow_stick_p2 = Point(200, 240)
    arrow_stick_p3 = Point(800, 260)
    arrow_stick_p4 = Point(800, 240)
    arrow_stick = Polygon(arrow_stick_p1, arrow_stick_p2, arrow_stick_p4, arrow_stick_p3)

    arrow_feather_p1 = Point(800,280)
    arrow_feather_p2 = Point(850, 280)
    arrow_feather_p3 = Point(825, 250)
    arrow_feather_p4 = Point(850, 220)
    arrow_feather_p5 = Point(800, 220)
    arrow_feather = Polygon(arrow_feather_p1, arrow_feather_p2, arrow_feather_p3, arrow_feather_p4, arrow_feather_p5)

    happy = Text(Point(100, 100), "Happy Valentine's Day!")
    happy.draw(win)
    happy.setFill('white')

    arrow_head.draw(win)
    arrow_stick.draw(win)
    arrow_feather.draw(win)
    triangle.draw(win)
    left_circle.draw(win)
    right_circle.draw(win)

    triangle.setFill('pink')

    left_circle.setFill('pink')
    right_circle.setFill('pink')
    left_circle.setOutline('pink')
    right_circle.setOutline('pink')

    arrow_head.setFill('red')
    arrow_stick.setFill('red')
    arrow_feather.setFill('red')
    arrow_head.setOutline('red')
    arrow_stick.setOutline('red')
    arrow_feather.setOutline('red')

    dx = -100
    dy = 0

    for i in range(10):
        arrow_head.move(dx, dy)
        arrow_stick.move(dx, dy)
        arrow_feather.move(dx, dy)
        sleep(.1)

    click = Text(Point(800, 500), "Click to close")
    click.draw(win)
    click.setFill('white')
    win.getMouse()
    win.close()