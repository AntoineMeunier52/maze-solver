from window import Window
from window_utils import Line, Point, Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(20, 20, 40, 40)
    cell2 = Cell(win)
    cell2.draw(40, 40, 60, 60)
    cell.draw_move(cell2)
    win.wait_for_close()

if __name__ == "__main__":
    main()
