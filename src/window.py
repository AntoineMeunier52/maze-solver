from tkinter import Tk, BOTH, Canvas, Button, Entry, Label, Frame
from menu import Menu
class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title = "Maze solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = None
        self.__frame = None 
        self.__is_running = False

    def drawMenu(self):
       print("draw menu")
       menu = Menu(self.__root)
       menu.draw()
       print("out of menu")
       return
        
    def drawMaze(self):
        print("draw maze")
        self.clear_view()
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        return

    def clear_view(self):
        #clear the root window before show maze or menu
        if self.__frame:
            self.__frame.destroy()
            self.__frame = None
        if self.__canvas:
            self.__canvas.destroy()
            self.__canvas = None

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        #don't close the windown directly
        while self.__is_running:
            self.redraw()
        print("The window is now close")
        return

    def close(self):
        self.__is_running = False
        print("Closing the window")
        return

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)
