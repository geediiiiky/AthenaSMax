from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle

class Separator(Widget):
    def __init__(self, **kwargs):
        self.color = kwargs.pop('color', (1,1,1,1))
        self.size_hint_y = None
        self.thickness = kwargs.pop('thickness', 2)
        self.margin = kwargs.pop('margin', (2, 4, 2, 5))    #left top right bottom
        self.orientation = kwargs.pop('orientation', 'horizontal')
        if self.orientation == 'horizontal':
            self.height = self.margin[1] + self.margin[3] + self.thickness
        else:
            self.width = self.margin[0] + self.margin[2] + self.thickness
        super(Separator, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.update_sep()
        self.bind(pos=self.update_sep, size=self.update_sep)
                                  
    def update_sep(self, *args):
        self.rect.pos = (self.x +self.margin[0], self.y + self.margin[3])
        self.rect.size = (self.width - self.margin[0] - self.margin[2], self.height - self.margin[1] - self.margin[3])