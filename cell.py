from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        if undo:
            color = "LightBlue1"
        else:
            color = "red"
        line = Line(
            Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2),
            Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        )
        self._win.draw_line(line, color)