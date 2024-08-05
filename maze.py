from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()

    def _create_cells(self):
        for row in range(self.num_rows):
            rows = []
            for col in range(self.num_cols):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                rows.append(Cell(x1, y1, x2, y2, win=self.win))
            self._cells.append(rows)
        #enumerate provides both the index and the value of said index
        if self.win is not None:
            for row_index, row in enumerate(self._cells): 
                for col_index, col in enumerate(row):
                    self._draw_cell(row_index, col_index)

    def reset(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def is_solved(self):
        return all(cell.is_visited() for row in self._cells for cell in row)

    def _draw_cell(self, row, col, wall_color="black"):
        x_position = self.x1 + col * self.cell_size_x
        y_position = self.y1 + row * self.cell_size_y 

        cell = self._cells[row][col]
        cell.x1 = x_position
        cell.y1 = y_position
        cell.x2 = x_position + self.cell_size_x
        cell.y2 = y_position + self.cell_size_y

        cell.draw(wall_color=wall_color)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[self.num_rows - 1][self.num_cols - 1]

        top_left_cell.remove_wall('top')
        bottom_right_cell.remove_wall('bottom')

        self._draw_cell(0, 0, wall_color="white")
        self._draw_cell(self.num_rows-1, self.num_cols-1, wall_color="white")