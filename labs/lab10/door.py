'''
Lex King
lab10.py
this makes the door
this is my code
'''

from graphics import Text

class Door:
    def __int__(self, shape, text, secret):
        self.shape = shape
        self.text = Text(shape.getCenter(), text)
        self.secret = secret

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def un_draw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x1 = self.shape.getP1().getX()
        x2 = self.shape.getP2().getX()
        y1 = self.shape.getP1().getY()
        y2 = self.shape.getP2().getY()
        if x1 <= point.getX() <= x2 and y1 <= point.getY() <= y2:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret

