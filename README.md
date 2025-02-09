# Binary Puzzle Solver (10x10)

A Python-based solution for solving 10x10 [binary puzzles](https://en.wikipedia.org/wiki/Takuzu), also known as Binary Sudoku. The goal of this puzzle is to fill a 10x10 grid with only two symbols (e.g., X and O) while adhering to the follwing rules:
- Each row and each column must contain an equal number of X and O.
- More than two of the same symbols can't be adjacent.
- Each row and column is unique.

## Initialize with a 10x10 grid (0 for empty cells)
The inputs are given as two lists. Each one containing the coordinates of the X and O given in the puzzle. The coordinates are tuples representing the x and y coordinate of the symbol on the grid. The grid coordinate starts at 0 and ends at 9, such that the coordinate of the upper left case is (0,0) and the bottom right is (9,9). 

## Algorithm
The solver uses a combination of:

Backtracking for brute-force searching.
Constraint Propagation to reduce possibilities before applying backtracking.
Key Features:
Detects invalid puzzles early during solving.

Efficiently skips impossible numbers based on row and column constraints.
