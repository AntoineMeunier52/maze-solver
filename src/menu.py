from tkinter import *
from tkinter import ttk

class Menu:
	def __init__(self, root, callback):
		self._frame = Frame(root, bg="white", height=100, width=200)
		self._start_callback = callback
		self.is_visible = False

		self.maze_x = IntVar()
		self.maze_y = IntVar()
		self.maze_x.set(10)
		self.maze_y.set(10)

		self._is_valid_size = True
		self._size_error = Label(self._frame, text="your maze size is not valid", font=("roboto", 12), bg="white", fg="red")
		#self.maze_size_x = IntVar(10)
		#self.maze_size_y = IntVar(10)
		#self.algo = StringVar("DFS")

		self.build_menu()

	def build_menu(self):
		Label(self._frame, text="Maze Solver", font=("roboto", 40), bg="white", fg="black").grid(row=0)
		maze_size_frame = Frame(self._frame, width=200, height=100, bg="white")
		maze_size_frame.grid(row=1)
		Label(maze_size_frame, text="Enter the size of the maze", font=("roboto", 16), bg="white", fg="black").grid(row=0, column=0)
		Label(maze_size_frame, text="X and Y must be between 10 and 40.", font=("roboto", 10), bg="white", fg="black").grid(row=1, column=0)

		x_y_frame = Frame(maze_size_frame, width=200, height=100, bg="white")
		x_y_frame.grid(row=2)
		Label(x_y_frame, text="X: ", bg="white", fg="Black", font=("roboto", 12)).grid(row=0, column=0)
		Entry(x_y_frame, textvariable = self.maze_x, width=5, bg="white", fg="black", font=("roboto", 12)).grid(row=0, column=1)
		Label(x_y_frame, text="Y: ", bg="white", fg="Black", font=("roboto", 12)).grid(row=0, column=2)
		Entry(x_y_frame, textvariable = self.maze_y, width=5, bg="white", fg="black", font=("roboto", 12)).grid(row=0, column=3)


		Button(self._frame, text="change view", command=self._start_maze).grid(row=2)

	def _check_maze_size(self):
		maze_size_x = self.maze_x.get()
		maze_size_y = self.maze_y.get()
		print("maze_x", maze_size_x, "maze_y", maze_size_y < 10)
		if (maze_size_x > 40 or maze_size_y > 40) or (maze_size_x < 10 or maze_size_y < 10):
			self._is_valid_size = False
			return
		self._is_valid_size = True

	def _start_maze(self):
		self._check_maze_size();
		if self._is_valid_size:
			print("callback")
			self._is_valid_size = True
			self._size_error.grid_forget()
			self._start_callback()
			return
		self._size_error.grid(row=3)

	def show(self):
		self.is_visible = True
		self._frame.pack(expand=YES)

	def destroy(self):
		self.is_visible = False
		self._frame.pack_forget()