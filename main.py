from graphics import Window, Line, Point
from nicegui import ui
from maze import Maze
from cell import Cell

def main():
    dimensions = (800, 600)  # Window size
    start_pos = (10, 10)     # Starting position
    grid_size = (11, 11)     # Grid dimensions
    
    # Assuming Window manages a graphics window interface, ensure all dependencies are correctly imported
    window = Window(*dimensions)

    # Adjust cell sizes based on the window dimensions and grid size
    cell_size = (
        (dimensions[0] - 20) // grid_size[1],
        (dimensions[1] - 20) // grid_size[0]
    )

    # Initialize the Maze with window support
    maze = Maze(*start_pos, *grid_size, *cell_size, win=window)

    # Print the initial maze configuration
    maze.print_maze_config()

    # Generate the maze paths using recursive wall breaking
    maze._break_walls_r(0, 0)

    # Set up the visualization, ensuring it's ready before solving
    maze.visualize_maze()

    # Attempt to solve and visualize the maze
    solved = maze.solve()

    # Display result after solving
    print(f"Solved: {solved}")

    # Handle window management and wait to close
    window.wait_for_close()

if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run()
