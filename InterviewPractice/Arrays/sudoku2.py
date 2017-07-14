"""
Jordan Stein
7/9/2017

Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

Input/Output

[time limit] 4000ms (py)
"""

def sudoku2(grid):

    # check rows
    for row in grid:
        for val in row:
            if row.count(val) > 1 and val != '.':
                return False

    # check columns
    rotated = list(reversed(zip(*grid)))
    for col in rotated:
        for val in col:
            if col.count(val) > 1 and val != '.':
                return False

    # check 3x3 submatrixs
    subMatrix = []
    for i in range(0,7,3):
        for j in range(0,7,3):
            subMatrix.append(grid[i][j])
            subMatrix.append(grid[i][j+1])
            subMatrix.append(grid[i][j+2])
            subMatrix.append(grid[i+1][j])
            subMatrix.append(grid[i+1][j+1])
            subMatrix.append(grid[i+1][j+2])
            subMatrix.append(grid[i+2][j])
            subMatrix.append(grid[i+2][j+1])
            subMatrix.append(grid[i+2][j+2])
            
            for indx in range(0,9):
                if subMatrix.count(subMatrix[indx]) > 1 and subMatrix[indx] != '.':
                    return False
            subMatrix = []

    return True