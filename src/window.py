from tkinter import Tk, BOTH, Canvas
from window_utils import Line

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("The window is now close")

    def close(self):
        self.__is_running = False
        print("Closing the window")

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)
