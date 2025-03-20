from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(250,150), Point(60, 300))
    line2 = Line(Point(30,400), Point(300,450))
    win.draw_line(line, "red")
    win.draw_line(line2)
    win.wait_for_close()

main()