from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=0, width=0)
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

    def draw_line(self, x1, y1, x2, y2, fill_color="black"):
        self.__canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

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
            fill=fill_color, width=4
        )