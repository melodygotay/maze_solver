class Cell:
    width = 20
    height = 20

    def __init__(self, x1, y1, x2, y2, win=None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.walls = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True
        }
        self.visited = False

    def draw(self, wall_color="black"):
        if not self._win:
            raise ValueError("Window or canvas not defined")
        if self.walls['left']:
            self._win.create_line(self._x1, self._y1, self._x1, self._y2, fill=wall_color)
        if self.walls['right']:
            self._win.create_line(self._x2, self._y1, self._x2, self._y2, fill=wall_color)
        if self.walls['top']:
            self._win.create_line(self._x1, self._y1, self._x2, self._y1, fill=wall_color)
        if self.walls['bottom']:
            self._win.create_line(self._x1, self._y2, self._x2, self._y2, fill=wall_color)

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

    def remove_wall(self, wall):
        self.walls[wall] = False

    def has_wall(self, wall):
        return self.walls[wall]

    '''   def remove_wall(self, wall):
        if wall == 'top':
            self.top = False
        elif wall == 'bottom':
            self.bottom = False
        elif wall == 'left':
            self.left = False
        elif wall == 'right':
            self.right = False
        else:
            raise ValueError("Invalid wall specified")'''