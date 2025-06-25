# Neural Nexus Puzzle

Neural Nexus Puzzle is a powerful AI-based solution framework for solving the classic **8-puzzle problem**. It incorporates multiple state-space search algorithms to demonstrate and evaluate the performance, trade-offs, and efficiency of various Artificial Intelligence techniques. This project is built using Python and is ideal for students, researchers, and enthusiasts interested in AI and search algorithms.

---

## About the Project

The 8-puzzle is a sliding tile puzzle that consists of a 3x3 grid with tiles numbered 1 through 8 and one blank space. The goal is to transform a given start state into a goal state by sliding the tiles, using the least number of moves or the optimal path based on the chosen search strategy.

This project provides a CPU-based implementation of the following AI search algorithms:

-  A* Search
-  Greedy Best-First Search
-  Breadth-First Search (BFS)
-  Depth-First Search (DFS)
-  Depth-Limited Search (DLS)
-  Iterative Deepening Search (IDS)
-  Uniform Cost Search (UCS)

Each algorithm is analyzed using metrics such as:
- Time taken
- Number of nodes generated and expanded
- Depth and cost of the solution path

Heuristic functions supported:
- **Manhattan Distance**
- **Misplaced Tile Count** *(optional future extension)*

---

## Features

- Modular design for easy integration and extension
- Clean terminal interface to choose algorithm and input states
- Visual trace of solution path and performance metrics
- Uses NumPy for efficient state management and copying
- Accurate heuristics to guide informed searches

---

## How to Run
- pip install numpy
- RUN python neuralpuzzle.py


