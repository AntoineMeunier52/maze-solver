from window import Window
from window_utils import Line, Point, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(250, 150, 10, 10, 30, 30, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
