from window_utils import Point, Line, Cell
import time


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [[None for j in range(num_rows)] for i in range(num_cols)]
        self._curr_x = x1
        self._curr_y = y1

    def _create_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j] = Cell(self._win)
                self._draw_cell(i, j);


    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * j)
        y1 = self._y1 + (self._cell_size_y * i)
        x2 = self._x1 + (self._cell_size_x * (j + 1))
        y2 = self._y1 + (self._cell_size_y * (i + 1))
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        #time.sleep(0.01)

