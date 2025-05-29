# 🧩 Maze Solver

Maze Solver is an educational Python project for drawing and solving mazes using graphics and search algorithms. This project was developed as part of boot.dev courses and is ideal for learning about classes, 2D lists, graphics, and basic algorithms.

---

## ✨ Features

- ✅ Dynamic creation of a grid (maze) with cells  
- ✅ Visualization of walls, entrance, and exit  
- ✅ Gradual drawing of the maze (animation)  
- ✅ Ability to add search and pathfinding algorithms (e.g. DFS, BFS — in progress)  
- ✅ Unit tests for logic verification (without graphics)  

---

## 🛠️ Project Structure

Maze-solver/
│
├── src/
│ ├── cell.py # Class representing a single maze cell
│ ├── maze.py # Class representing the entire maze grid
│ ├── main.py # Main program to run and display the maze
│ ├── window.py # Wrapper for drawing (GUI window)
│ └── tests.py # Unit tests to verify maze logic
│
├── README.md # This file
├── .gitignore # Git ignore rules

---

## 📦 How to Run

Clone the repository:

```bash
git clone https://github.com/miARTre/Maze-solver.git
cd Maze-solver/src

(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows

Run the main program (for example, if you have main.py as entry point):
python main.py

✅ Testing
The project includes basic unit tests for maze logic:
python -m unittest tests.py
The tests do not cover drawing, only logic such as number of cells and wall removal.

🧱 Classes
Cell
Represents one maze cell. Stores walls and knows how to draw itself.

Maze
Consists of many cells in a grid. Responsible for creating cells, drawing, and breaking walls for entrance/exit.

Window
Simple GUI layer for drawing lines and showing animations.

🔧 Work in Progress
Adding maze-solving algorithms (DFS, BFS, A*)
Visualizing the path through the maze
Interactive random maze generation

👨‍💻 Author
Made with 🧠 by miARTre – part of Boot.dev courses.
All comments and pull requests are welcome!