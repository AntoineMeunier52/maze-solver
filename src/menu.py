from tkinter import *
from tkinter import ttk

class Menu:
	def __init__(self, root, callback):
		self._frame = Frame(root, bg="white", height=100, width=200)
		self._start_callback = callback
		self.is_visible = False

		self.maze_x = IntVar()
		self.maze_y = IntVar()
		self.maze_x.set(40)
		self.maze_y.set(40)

		self.algo = StringVar()
		self.algo.set("DFS")

		self._is_valid_size = True
		self._size_error = Label(self._frame, text="your maze size is not valid", font=("roboto", 12), bg="white", fg="red")

		self.build_menu()

	def build_menu(self):
		Label(self._frame, text="Maze Solver", font=("roboto", 40), bg="white", fg="black").grid(row=0, pady=10)
		maze_size_frame = Frame(self._frame, width=200, height=100, bg="white")
		maze_size_frame.grid(row=1, pady=10)
		Label(maze_size_frame, text="Enter the size of the maze", font=("roboto", 16), bg="white", fg="black").grid(row=0, column=0, pady=5)
		Label(maze_size_frame, text="X and Y must be between 10 and 40.", font=("roboto", 10), bg="white", fg="black").grid(row=1, column=0, pady=5)

		x_y_frame = Frame(maze_size_frame, width=200, height=100, bg="white")
		x_y_frame.grid(row=2, pady=10)
		Label(x_y_frame, text="X: ", bg="white", fg="Black", font=("roboto", 12)).grid(row=0, column=0)
		Entry(x_y_frame, textvariable = self.maze_x, width=5, bg="white", fg="black", font=("roboto", 12), justify="center").grid(row=0, column=1)
		Label(x_y_frame, text="Y: ", bg="white", fg="Black", font=("roboto", 12)).grid(row=0, column=2)
		Entry(x_y_frame, textvariable = self.maze_y, width=5, bg="white", fg="black", font=("roboto", 12), justify="center").grid(row=0, column=3)

		combobox_frame = Frame(self._frame, width=200, height=100, bg="white")
		combobox_frame.grid(row=3, pady=10)
		combobox = ttk.Combobox(combobox_frame, width=20, textvariable=self.algo)
		combobox["values"] = ("DFS", "oriented DFS", "BFS", "A*", "DIJKSTAR")
		combobox.grid(row=3)

		Button(self._frame, text="change view", command=self._start_maze).grid(row=4, pady=5)

	def _check_maze_size(self):
		maze_size_x = self.maze_x.get()
		maze_size_y = self.maze_y.get()
		if (maze_size_x > 40 or maze_size_y > 40) or (maze_size_x < 10 or maze_size_y < 10):
			self._is_valid_size = False
			return
		self._is_valid_size = True

	def _start_maze(self):
		self._check_maze_size();
		if self._is_valid_size:
			self._is_valid_size = True
			self._size_error.grid_forget()
			self._start_callback(self.maze_x.get(), self.maze_y.get(), self.algo.get())
			return
		self._size_error.grid(row=5)

	def show(self):
		self.is_visible = True
		self._frame.pack(expand=YES)

	def destroy(self):
		self.is_visible = False
		self._frame.pack_forget()