from tkinter import *
import time
import random
import heapq

from window_utils import Cell, Line

class Maze():
    def __init__(self, root, callback, redraw, width, height):
        self._frame = Frame(root, bg="white", height=100, width=200)
        self._start_callback = callback
        self.is_visible = False
        self.redraw = redraw
        self.width = width
        self.height = height
        self._canvas = None

    def show(self, x, y, algo):
        self.is_visible = True
        cell_size_x = (self.width - 2 * 50) / x
        cell_size_y = (self.height - 2 * 50) / y
        self._canvas = Canvas(self._frame, bg="white", width=self.width, height=self.height)
        self._frame.pack(expand=YES)
        self._canvas.pack(fill=BOTH, expand=1)
        maze = Maze_solver(50, 50, x, y, cell_size_x, cell_size_y, self.redraw, self.draw_line, self._canvas)
        maze.solve(algo)


    def destroy(self):
        self.is_visible = False
        self._frame.pack_forget()

    def draw_line(self, line, color):
        line.draw(self._canvas, color)

class Maze_solver():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            redraw,
            draw_line,
            root
    ):
        self._x1 = x1
        self._y1 = y1
        self._rows = num_rows
        self._cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._redraw = redraw
        self._draw_line = draw_line
        self._cells = [[Cell(draw_line) for j in range(num_cols)] for i in range(num_rows)]
        self._curr_x = x1
        self._curr_y = y1
        self._canvas = root

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
        x1 = self._x1 + (self._cell_size_x * j)
        y1 = self._y1 + (self._cell_size_y * i)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(0.0)

    def _animate(self, timing):
        self._redraw()
        time.sleep(timing)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw_breaking_wall()
        self._cells[self._rows - 1][self._cols - 1].has_bottom_wall = False
        self._cells[self._rows - 1][self._cols - 1].draw_breaking_wall()
        self._animate(0.0)

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
                self._animate(0.01)
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

    def solve(self, algo=None):
        if algo == "DFS":
            return self._solve_DFS(0, 0)
        if algo == "oriented DFS":
            return self._solve_DFS_opti(0, 0)
        if algo == "BFS":
            return self._solve_BFS(0, 0)
        if algo == "A*":
            return self._solve_Astar()
        if algo == "DIJKSTAR":
            self._canvas.create_text(400, 20, text="BFS not already implement", fill="red", font=("robot", 20 ))
        if not algo:
            self._canvas.create_text(400, 20, text="No algo selected", fill="red", font=("robot", 20 ))

    def _solve_BFS(self, i, j):
        queue = [(i, j)]
        parent = { (i, j): None }
        goal = (self._rows -1, self._cols -1)

        while queue:
            print("================> animate")
            self._animate(0.02)
            i, j = queue.pop(0)
            if (i, j) == goal:
                break

            self._cells[i][j].visited = True
            if (
                i > 0 
                and not self._cells[i - 1][j].visited 
                and not self._cells[i][j].has_top_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i - 1][j], True)
                    parent[(i - 1, j)] = (i, j)
                    queue.append((i - 1, j))
            if (
                i < self._rows - 1
                and not self._cells[i + 1][j].visited
                and not self._cells[i][j].has_bottom_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i + 1][j], True)
                    parent[(i + 1, j)] = (i, j)
                    queue.append((i + 1, j))
            if (
                j > 0
                and not self._cells[i][j - 1].visited
                and not self._cells[i][j].has_left_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)
                    parent[(i, j - 1)] = (i, j)
                    queue.append((i, j - 1))
            if (
                j < self._cols - 1
                and not self._cells[i][j + 1].visited
                and not self._cells[i][j].has_right_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i][j + 1], True)
                    parent[(i, j + 1)] = (i, j)
                    queue.append((i, j + 1))


        #check if maze is solved
        if goal not in parent:
            return False
        
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        for (i, j), (k, l) in zip(path, path[1:]):
            self._cells[i][j].draw_move(self._cells[k][l])
        return True

    def _solve_DFS_opti(self, i, j):
        queue = [(i, j)]
        parent = { (i, j): None }
        goal = (self._rows -1, self._cols -1)

        while queue:
            self._animate(0.02)
            i, j = queue.pop()
            if (i, j) == goal:
                break

            self._cells[i][j].visited = True
            if (
                i > 0 
                and not self._cells[i - 1][j].visited 
                and not self._cells[i][j].has_top_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i - 1][j], True)
                    parent[(i - 1, j)] = (i, j)
                    queue.append((i - 1, j))
            if (
                i < self._rows - 1
                and not self._cells[i + 1][j].visited
                and not self._cells[i][j].has_bottom_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i + 1][j], True)
                    parent[(i + 1, j)] = (i, j)
                    queue.append((i + 1, j))
            if (
                j > 0
                and not self._cells[i][j - 1].visited
                and not self._cells[i][j].has_left_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)
                    parent[(i, j - 1)] = (i, j)
                    queue.append((i, j - 1))
            if (
                j < self._cols - 1
                and not self._cells[i][j + 1].visited
                and not self._cells[i][j].has_right_wall
            ):
                    self._cells[i][j].draw_move(self._cells[i][j + 1], True)
                    parent[(i, j + 1)] = (i, j)
                    queue.append((i, j + 1))

        print("out of main loop")
        #check if maze is solved
        if goal not in parent:
            return False
        
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        for (i, j), (k, l) in zip(path, path[1:]):
            self._cells[i][j].draw_move(self._cells[k][l])
        return True

    def _solve_DFS(self, i, j):
        self._animate(0.02)
        self._cells[i][j].visited = True
        if i == self._rows - 1 and j == self._cols - 1:
            return True

        if (
            i > 0 
            and not self._cells[i - 1][j].visited 
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_DFS(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self._rows - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_DFS(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_DFS(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self._cols - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_DFS(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

    #count a the current cell to the end of the maze
    def _A_star_heuristic(self, a, b):
         return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def _solve_Astar(self):
        start = (0, 0)
        goal = (self._rows - 1, self._cols - 1)

        open_set = []
        heapq.heappush(open_set, (0, start)) #(f_score, node)

        g_score = {start: 0}
        parent = {start: None}

        while open_set:
            self._animate(0.02)

            _, current = heapq.heappop(open_set)
            i, j = current

            if current == goal:
               break
            if self._cells[i][j].visited:
                continue
            self._cells[i][j].visited = True

            if (
                i > 0 
                and not self._cells[i - 1][j].visited 
                and not self._cells[i][j].has_top_wall
            ):
                tentative_g = g_score[current] + 1
                neighbor = (i - 1, j)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                     g_score[neighbor] = tentative_g
                     f_score = tentative_g + self._A_star_heuristic(neighbor, goal)
                     heapq.heappush(open_set, (f_score, neighbor))
                     parent[neighbor] = current
                     self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]], True)
            if (
                i < self._rows - 1
                and not self._cells[i + 1][j].visited
                and not self._cells[i][j].has_bottom_wall
            ):
                tentative_g = g_score[current] + 1
                neighbor = (i + 1, j)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                     g_score[neighbor] = tentative_g
                     f_score = tentative_g + self._A_star_heuristic(neighbor, goal)
                     heapq.heappush(open_set, (f_score, neighbor))
                     parent[neighbor] = current
                     self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]], True)
            if (
                j > 0
                and not self._cells[i][j - 1].visited
                and not self._cells[i][j].has_left_wall
            ):
                tentative_g = g_score[current] + 1
                neighbor = (i, j - 1)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                     g_score[neighbor] = tentative_g
                     f_score = tentative_g + self._A_star_heuristic(neighbor, goal)
                     heapq.heappush(open_set, (f_score, neighbor))
                     parent[neighbor] = current
                     self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]], True)
            if (
                j < self._cols - 1
                and not self._cells[i][j + 1].visited
                and not self._cells[i][j].has_right_wall
            ):
                tentative_g = g_score[current] + 1
                neighbor = (i, j + 1)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                     g_score[neighbor] = tentative_g
                     f_score = tentative_g + self._A_star_heuristic(neighbor, goal)
                     heapq.heappush(open_set, (f_score, neighbor))
                     parent[neighbor] = current
                     self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]], True)

        if goal not in parent:
             return False
        
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        for (i, j), (k, l) in zip(path, path[1:]):
            self._cells[i][j].draw_move(self._cells[k][l])
        return True