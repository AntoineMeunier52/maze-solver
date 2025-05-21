from tkinter import *
from tkinter import ttk

class Menu:
	def __init__(self, root):
		self._frame = Frame(root, bg="lightgray")

		Label(self._frame, text="Maze Solver").pack(pady=10)
		Label(self._frame, text="Enter the size of the maze").pack()

		self.x = IntVar()
		self.y = IntVar()

		Label(self._frame, text="X:").pack()
		self.x_entry = Entry(self._frame, textvariable=self.x).pack()

		Label(self._frame, text="Y:").pack()
		self.y_entry = Entry(self._frame, textvariable=self.y).pack()

		Label(self._frame, test="select algo").pack()
		self.algo = StringVar(value="DFS")
		self.algo_combo = ttk.Combobox(self._frame, textvariable=self.algo, state="readonly").pack()
		self.algo_select["values"] = ["DFS", "BFS", "A*", "Dijkstra"]
		
		Button(self._frame, text="Start", command=self._on_start).pack(pady=10)
	
	def _on_start():
		
		return