from tkinter import Tk, BOTH, Canvas, Button, Entry, Label, Frame
from menu import Menu
from maze import Maze

class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.geometry(f"{width}x{height}")
        self._root.minsize(width, height)
        self._root.title("Maze Solver")
        self._root.config(background="white")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._menu = Menu(self._root, self._switch_view)
        self._maze = Maze(self._root, self._switch_view, self.redraw, width, height)

        self._canvas = None
        self._frame = None 
        self._is_running = False
        self._can_change_view = False
        
        self.maze_x = 14
        self.maze_y = 16
        self.algo = "DFS"

        self._menu.show()

    def _switch_view(self, maze_x=None, maze_y=None, algo=None):
        if (maze_x and maze_y and algo):
            self.maze_x = maze_x
            self.maze_y = maze_y
            self.algo = algo
        self._can_change_view=True

    def _change_view(self, ):
        if self._menu.is_visible:
            self._menu.destroy()
            self._maze.show(self.maze_x, self.maze_y, self.algo)
        elif self._maze.is_visible:
            self._maze.destroy()
            self._menu.show()

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True
        #don't close the windown directly
        while self._is_running:
            if self._can_change_view:
                self._change_view()
                self._can_change_view = False
            print("loop")
            self.redraw()
        print("The window is now close")
        return

    def close(self):
        self._is_running = False
        print("Closing the window")
        return

    def draw_line(self, line, color):
        line.draw(self._canvas, color)
