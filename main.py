from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(100, 100, 150, 150)
    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(200, 100, 250, 150)
    c3 = Cell(win)
    c3.has_right_wall = False
    c3.draw(100, 300, 150, 350)
    c4 = Cell(win)
    c4.has_bottom_wall = False
    c4.draw(200, 300, 250, 350)
    c5 = Cell(win)
    c5.has_left_wall = False
    c5.draw(100, 500, 150, 550)

    c1.draw_move(c2)

    c3.draw_move(c4, True)

    c3.draw_move(c5)

    win.wait_for_close()

main()