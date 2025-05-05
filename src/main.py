from window import Window
from window_utils import Line, Point, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(100, 100, 200, 200, 5, 5, win)
    maze._create_cells()
    win.wait_for_close()

if __name__ == "__main__":
    main()
