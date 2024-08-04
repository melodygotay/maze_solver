from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("closing window...")
        #self.__root.destroy() 

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x #x-coordinate (horizontal) in pixels of the point
        self.y = y #y-coordinate (vertical) in pixels of the point

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill=fill_color, width=2
        )

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
        print(f"Cell initialized with window: {self._win}")

    def draw(self):
        print(f"Drawing cell with window: {self._win}")
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

    def draw_move(self, to_cell, undo=False):
        center_x_self = self._x1 + Cell.width / 2
        center_y_self = (self._y1 + self._y2) / 2
        center_x_to = to_cell._x1 + Cell.width / 2
        center_y_to = (to_cell._y1 + to_cell._y2) / 2

        line_color = "gray" if undo else "red"

        if not self._win:
            raise ValueError("Window or canvas not defined")
        self._win.create_line(center_x_self, center_y_self, center_x_to, center_y_to, fill=line_color)