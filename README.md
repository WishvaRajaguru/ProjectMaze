# 🧠 Maze Solver: Queue & Stack Agent

A simple maze-solving project in Python where an **Agent navigates a grid-based maze** using two classic algorithms:

- **First-In-First-Out (FIFO)** – Queue-based approach (BFS-style traversal)  
- **Last-In-First-Out (LIFO)** – Stack-based approach (DFS-style traversal)

The project also includes functionality to **generate and save a solution image**, visually showing the agent's path.

---

## ✨ Features

- 🧱 Fixed-size grid maze layout
- 🤖 Agent solves the maze using:
  - **Queue (FIFO)** — explores level-by-level (like BFS)
  - **Stack (LIFO)** — explores depth-first (like DFS)
- 🖼️ Solution rendering using **Pillow (PIL)** with:
  - Walls, paths, and visited nodes shown in color
  - Start and goal clearly marked
- 💾 Option to **save the final solved maze as an image**

---

## 📦 Technologies Used

- **Python 3.x**
- [`Pillow`](https://pypi.org/project/Pillow/) – for drawing and exporting images
- Pure Python logic for maze generation and traversal

---

## 🚀 Use Cases

This project is ideal for:

- Learning fundamental **search algorithms** (BFS vs DFS)
- Practicing graphics and visualization in Python
- Comparing search strategies in a visual way
- Building a base for more advanced **AI navigation agents**

---

📷 Sample Output (will be added)

## 🏁 Getting Started

Follow these steps to set up and run the project:

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/WishvaRajaguru/ProjectMaze.git
cd [to-download-location]
```

### 2. 📦 Install Dependencies

Make sure you have Python 3 installed, then install the required package:

```bash
pip install Pillow
```

3. 🚀 Run the Maze Solver
To run the program and generate a solution image:

```bash
python main.py
```

This will:

- Load or generate a maze
- Solve it using both queue (FIFO) and stack (LIFO) strategies
- Generate and display or save the solution image


### ENJOY....
