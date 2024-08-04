import tkinter as tk
from graphics import Cell

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Creating some cells and ensuring the canvas is correctly passed
cell1 = Cell(50, 50, 70, 70, win=canvas)
cell2 = Cell(150, 150, 170, 170, win=canvas)

# Draw the cell borders
cell1.draw()
cell2.draw()

# Test moving from cell1 to cell2 with default undo=False
cell1.draw_move(to_cell=cell2)
# Test moving from cell2 to cell1 with undo=True
cell2.draw_move(to_cell=cell1, undo=True)

root.mainloop()