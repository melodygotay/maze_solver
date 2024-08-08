from cell import Cell
import time, random
import tkinter as tk

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        # Initialize the 2D grid of cells
        self._cells = [
            [Cell(x1 + j * cell_size_x, y1 + i * cell_size_y, 
                x1 + (j + 1) * cell_size_x, y1 + (i + 1) * cell_size_y, win) 
            for j in range(num_cols)]
            for i in range(num_rows)
        ]

        self._create_cells()  # Assuming this initializes or modifies cells further
        self.initialize_open_path()  # Ensure at least one path is open at start
        self._break_entrance_and_exit()  # Create entrances and exits

    def initialize_open_path(self):
        # Ensure that (0, 0) has an open path
        if self.num_cols > 1:
            self._cells[0][0].walls['right'] = False
            self._cells[0][1].walls['left'] = False
        elif self.num_rows > 1:
            self._cells[0][0].walls['bottom'] = False
            self._cells[1][0].walls['top'] = False

    def _create_cells(self):
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

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[self.num_rows - 1][self.num_cols - 1]

        top_left_cell.remove_wall('top')
        bottom_right_cell.remove_wall('bottom')

        self._draw_cell(0, 0, wall_color="white")
        self._draw_cell(self.num_rows-1, self.num_cols-1, wall_color="white")

    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        print(f"Breaking walls at ({row}, {col})")

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
            if (
                0 <= new_row < self.num_rows and
                0 <= new_col < self.num_cols and
                not self._cells[new_row][new_col].visited
            ):
                # Break walls between current and new cells
                if col < new_col:  # Moving right
                    if self._cells[row][col].walls['right']:
                        print(f"Breaking right wall of ({row}, {col}) and left wall of ({new_row}, {new_col})")
                        self._cells[row][col].walls['right'] = False
                        self._cells[new_row][new_col].walls['left'] = False
                elif col > new_col:  # Moving left
                    if self._cells[row][col].walls['left']:
                        print(f"Breaking left wall of ({row}, {col}) and right wall of ({new_row}, {new_col})")
                        self._cells[row][col].walls['left'] = False
                        self._cells[new_row][new_col].walls['right'] = False
                elif row < new_row:  # Moving down
                    if self._cells[row][col].walls['bottom']:
                        print(f"Breaking bottom wall of ({row}, {col}) and top wall of ({new_row}, {new_col})")
                        self._cells[row][col].walls['bottom'] = False
                        self._cells[new_row][new_col].walls['top'] = False
                elif row > new_row:  # Moving up
                    if self._cells[row][col].walls['top']:
                        print(f"Breaking top wall of ({row}, {col}) and bottom wall of ({new_row}, {new_col})")
                        self._cells[row][col].walls['top'] = False
                        self._cells[new_row][new_col].walls['bottom'] = False

                # Recurse into the chosen cell
                self._break_walls_r(new_row, new_col)


    def _reset_cells_visited(self):
        for rows in self._cells:
            for cols in rows:
                cols.visited = False

    def _solve_r(self, row, col):
        print(f"Visiting cell: ({row}, {col})")
        
        # Check if the current cell is already visited
        if self._cells[row][col].visited:
            print(f"Cell ({row}, {col}) has already been visited. Backtracking.")
            return False
        
        # Visual feedback for visiting the cell
        self.app._draw_visiting_mark(row, col, "blue")  # Assume a mark method for tracking steps
        self._animate()  # Refresh the view
        
        # Mark this cell as visited
        self._cells[row][col].visited = True

        # Check if we've reached the goal
        if row == self.num_rows - 1 and col == self.num_cols - 1:
            print(f"Reached goal at: ({row}, {col})")
            return True

        moves = {
            'left': (0, -1),
            'right': (0, 1),
            'top': (-1, 0),
            'bottom': (1, 0)
        }

        for direction, (d_row, d_col) in moves.items():
            next_row = row + d_row
            next_col = col + d_col

            if 0 <= next_row < self.num_rows and 0 <= next_col < self.num_cols:
                wall_state = self._cells[row][col].walls[direction]
                visited_state = self._cells[next_row][next_col].visited
                
                print(f"Checking move {direction} to ({next_row}, {next_col}): Wall: {wall_state}, Visited: {visited_state}")

                if not wall_state and not visited_state:  # No wall and not visited
                    print(f"Trying {direction} to ({next_row}, {next_col})")
                    if self._solve_r(next_row, next_col):
                        self.app._draw_visiting_mark(row, col, "green")  # Path to solution
                        self._animate()
                        return True
                    else:
                        self.app._draw_visiting_mark(row, col, "red")  # Backtracking visualization
                        self._animate()
                        print(f"Backtracking from: ({next_row}, {next_col}) to ({row}, {col})")

        return False  # No valid moves found
    
    def solve(self):
        self.reset()  # Reset visited cells before solving
        return self._solve_r(0, 0)

    def print_maze_config(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                walls = self._cells[r][c].walls
                print(f"Cell ({r}, {c}): Top: {walls['top']}, Bottom: {walls['bottom']}, Left: {walls['left']}, Right: {walls['right']}")

    def visualize_maze(self):
        # Initialize MazeApp here to ensure `app` is known
        self.app = MazeApp(self._cells, self.cell_size_x, self.cell_size_y)
        self.app.draw_maze()  # Initial maze draw
        self.solve()  # Solve after setup
        self.app.run()  # Start the event loop

class MazeApp:
    def __init__(self, cells, cell_size_x, cell_size_y):
        self.cells = cells
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.root = tk.Tk()
        self.root.title("Maze Visualizer")
        self.canvas = tk.Canvas(self.root, width=cell_size_x * len(cells[0]), height=cell_size_y * len(cells))
        self.canvas.pack()

    def draw_maze(self):
        for row_index, row in enumerate(self.cells):
            for col_index, cell in enumerate(row):
                x0 = col_index * self.cell_size_x
                y0 = row_index * self.cell_size_y
                x1 = x0 + self.cell_size_x
                y1 = y0 + self.cell_size_y

                # Draw the top wall
                if cell.walls['top']:
                    self.canvas.create_line(x0, y0, x1, y0, fill="black", width=2)
                # Draw the bottom wall
                if cell.walls['bottom']:
                    self.canvas.create_line(x0, y1, x1, y1, fill="black", width=2)
                # Draw the left wall
                if cell.walls['left']:
                    self.canvas.create_line(x0, y0, x0, y1, fill="black", width=2)
                # Draw the right wall
                if cell.walls['right']:
                    self.canvas.create_line(x1, y0, x1, y1, fill="black", width=2)

    def _draw_visiting_mark(self, row, col, color):
        """Draw a small centered mark to indicate cell visitation."""
        grid_margin = 4  # Margin to make a thinner mark
        x0 = col * self.cell_size_x + grid_margin
        y0 = row * self.cell_size_y + grid_margin
        x1 = (col + 1) * self.cell_size_x - grid_margin
        y1 = (row + 1) * self.cell_size_y - grid_margin
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)
        self.canvas.update_idletasks()  # Update the display
        time.sleep(0.05)  # Pause for a short duration

    def run(self):
        self.root.mainloop() 