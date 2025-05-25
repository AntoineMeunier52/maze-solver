# 🧭 Maze Solver with Tkinter

This project is a **maze generator and solver** built with **Python** and **Tkinter** for real-time visualization.
It automatically generates a random maze and then solves it using a pathfinding algorithm, all visualized step-by-step in a graphical window.

![Demo](maze-solver.gif)

## 🎮 Features

- ✅ Random maze generation
- ✅ Visual maze solving
- ✅ Adjustable grid size
- ✅ Algorithm Selection

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/AntoineMeunier52/maze-solver
   cd maze-solver
   python3 src/main.py
   ```
## Implemented Pathfinding Algorithms

This maze visualizer includes several classic pathfinding algorithms, each with unique characteristics. 
Below is a quick overview of their principles, advantages, and limitations.

### Depth-First Search (DFS)
- **Description**: Explores as far as possible along each path before backtracking.
- ✅ **Pros**:
  - Simple and fast to implement  
  - Can quickly find a solution in favorable mazes
- ❌ **Cons**:
  - Does not guarantee the shortest path  
  - May explore deeply into dead ends

---

### Directional DFS
- **Description**: DFS with prioritized directions (e.g., right/bottom first), simulating intelligent behavior.
- ✅ **Pros**:
  - Often faster in structured mazes  
  - Simple yet effective when directions are well chosen
- ❌ **Cons**:
  - Still non-optimal  
  - Performance depends on maze layout

---

### Breadth-First Search (BFS)
- **Description**: Explores all neighbors level by level, ensuring uniform depth.
- ✅ **Pros**:
  - Always finds the shortest path  
  - Robust and predictable
- ❌ **Cons**:
  - Can be slow due to exhaustive search  
  - Explores many unnecessary nodes

---

### A* Search
- **Description**: Like BFS but guided by a heuristic estimating the remaining distance to the goal.
- ✅ **Pros**:
  - Guaranteed shortest path  
  - Typically faster than BFS in large mazes
- ❌ **Cons**:
  - Slightly more complex to implement  
  - Efficiency depends on the quality of the heuristic
