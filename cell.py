class Cell:
    width = 20
    height = 20

    def __init__(self, x1, y1, x2, y2, left=True, right=True, top=True, bottom=True, win=None):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if not self._win:
            raise ValueError("Window or canvas not defined")
        if self.left:
            self._win.create_line(self._x1, self._y1, self._x1, self._y2)
        if self.right:
            self._win.create_line(self._x2, self._y1, self._x2, self._y2)
        if self.top:
            self._win.create_line(self._x1, self._y1, self._x2, self._y1)
        if self.bottom:
            self._win.create_line(self._x1, self._y2, self._x2, self._y2)

    def mark_as_visited(self):
        self.visited = True

    def is_visited(self):
        return self.visited

    def draw_move(self, to_cell, undo=False):
        center_x_self = self._x1 + Cell.width / 2
        center_y_self = (self._y1 + self._y2) / 2
        center_x_to = to_cell._x1 + Cell.width / 2
        center_y_to = (to_cell._y1 + to_cell._y2) / 2

        line_color = "gray" if undo else "red"

        if not self._win:
            raise ValueError("Window or canvas not defined")
        self._win.create_line(center_x_self, center_y_self, center_x_to, center_y_to, fill=line_color)