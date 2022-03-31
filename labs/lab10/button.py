'''
Lex King
lab10.py
this makes the button
this is my code
'''

from graphics import Text

class Button:
    def __int__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

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
        if point >= x1 and point <= x2 and point >= y1 and point <= y2:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
