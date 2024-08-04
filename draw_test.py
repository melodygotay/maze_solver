import tkinter as tk
from cell import Cell

# Create the main window and canvas
root = tk.Tk()
root.title("Cell Drawing Test with _win")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create and draw cells using the canvas as win

# Cell 1: Left, Top, Right walls (but no Bottom wall)
cell1 = Cell(50, 50, 100, 100, left=True, right=True, top=True, bottom=False, win=canvas)
cell1.draw()

# Cell 2: Top, Right, Bottom walls (but no Left wall)
cell2 = Cell(120, 50, 170, 100, left=False, right=True, top=True, bottom=True, win=canvas)
cell2.draw()

# Cell 3: Left, Bottom walls (but no Top or Right walls)
cell3 = Cell(190, 50, 240, 100, left=True, right=False, top=False, bottom=True, win=canvas)
cell3.draw()

# Cell 4: No walls
cell4 = Cell(260, 50, 310, 100, left=False, right=False, top=False, bottom=False, win=canvas)
cell4.draw()

# Cell 5: All walls
cell5 = Cell(330, 50, 380, 100, left=True, right=True, top=True, bottom=True, win=canvas)
cell5.draw()

# Optional: Add more test cases
# Cell 6: Only Left and Right walls
cell6 = Cell(50, 150, 100, 200, left=True, right=True, top=False, bottom=False, win=canvas)
cell6.draw()

# Cell 7: Only Top and Bottom walls
cell7 = Cell(120, 150, 170, 200, left=False, right=False, top=True, bottom=True, win=canvas)
cell7.draw()

# Cell 8: Left, Right, Bottom walls (no Top wall)
cell8 = Cell(190, 150, 240, 200, left=True, right=True, top=False, bottom=True, win=canvas)
cell8.draw()

# Run the application
root.mainloop()