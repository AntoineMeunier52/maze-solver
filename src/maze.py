from window_utils import Point, Line, Cell
import time
import random


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._rows = num_rows
        self._cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [[Cell(win) for j in range(num_cols)] for i in range(num_rows)]
        self._curr_x = x1
        self._curr_y = y1

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j);
        self._break_entrance_and_exit()


    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + (self._cell_size_x * j)
        y1 = self._y1 + (self._cell_size_y * i)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.0333)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw_breaking_wall()
        self._cells[self._rows - 1][self._cols - 1].has_bottom_wall = False
        self._cells[self._rows - 1][self._cols - 1].draw_breaking_wall()
        self._animate()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #check which cells need to be visite
            #top
            if i > 0 and not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            #left
            if j > 0 and not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            #bottom
            if i < self._rows - 1 and not self._cells[i + 1][j].visited:
                    to_visit.append([i + 1, j])
            #right
            if j < self._cols - 1 and not self._cells[i][j + 1].visited:
                    to_visit.append([i, j + 1])

            #if there no more cells to visit just draw and return
            if not to_visit:
                self._cells[i][j].draw_breaking_wall()
                self._animate()
                return

            #get a random direction
            random_dir = random.randrange(len(to_visit))
            next_cell = to_visit[random_dir]

            #break the wall between the current cell and the next cell to check
            #to bottom
            if next_cell[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            #to top
            if next_cell[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            #to right
            elif next_cell[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            #to left
            elif next_cell[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for rows in self._cells:
            for cell in rows:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._rows - 1 and j == self._cols - 1:
            return True

        if (
            i > 0 
            and not self._cells[i - 1][j].visited 
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self._rows - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self._cols - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
