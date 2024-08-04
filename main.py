from graphics import Window, Line, Point


def main():
    window = Window(800, 600)  # Create a window with width 800 and height 600
    
    # Create points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 300)
    p4 = Point(400, 100)
    
    # Create lines from points
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    
    # Draw lines on the window
    window.draw_line(line1, "red")
    window.draw_line(line2, "blue")
    
    # Wait for the window to close
    window.wait_for_close()

main()

#ON TO PAGE 5 OF THE ASSIGNMENT