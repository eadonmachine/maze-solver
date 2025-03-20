from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    c = Cell(win)
    c.draw(100, 100, 150, 150)
    c = Cell(win)
    c.has_top_wall = False
    c.draw(200, 100, 250, 150)
    c = Cell(win)
    c.has_right_wall = False
    c.draw(100, 300, 150, 350)
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(200, 300, 250, 350)
    c = Cell(win)
    c.has_left_wall = False
    c.draw(100, 500, 150, 550)
    win.wait_for_close()

main()