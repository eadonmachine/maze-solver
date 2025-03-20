from graphics import Window, Line, Point
from maze import Maze

def main():
    num_cols = 12
    num_rows = 10
    margin_x = 10
    margin_y = 10
    screen_width = 800
    screen_height = 600
    cell_size_x = (screen_width - 2 * margin_x) / num_cols
    cell_size_y = (screen_height - 2 * margin_y) / num_rows
    seed = None

    win = Window(screen_width, screen_height)

    maze = Maze(margin_x, margin_y, num_cols, num_rows, cell_size_x, cell_size_y, win, seed)

    win.wait_for_close()

main()