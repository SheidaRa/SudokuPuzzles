from queue import Empty
import tkinter as tk

from matplotlib.pyplot import grid

# window=tk.Tk()
# window.title(Sudoku Solver)
# window.geometry("300x200+10+20")
# window.mainloop()


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# prints the unsolved sudoku puzzle
def printBoard(Puzzle):
    for x in range(len(Puzzle)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(Puzzle[x])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(Puzzle[x][y])
            else:
                print(str(Puzzle[x][y]) + " ", end="")\


# determines whether the cell is empty
def isEmpty(Puzzle):
    for x in range(len(Puzzle)):
        for y in range(len(Puzzle[x])):
            if Puzzle[x][y] == 0:
                return (x,y)


# create a nested list with each list representing a row and each value being the coordinate of an empty cell
def emptyMatrix(Puzzle): # not needed in a recursive function
    gridList = []
    for x in range(len(Puzzle)):
        tupleList = []
        for y in range(len(Puzzle[x])):
            if Puzzle[x][y] == 0:
                tupleList.append((x,y))
        gridList.append(tupleList)
    return gridList


# checks validity of the cell across neighbors in the row
def validRow(Puzzle, cell, num):
    for a in range(len(Puzzle)):
        if Puzzle[cell[0]][a] == num and (cell[0], a) != cell:
            return False


# checks validity of the cell across neighbors in the column
def validCol(Puzzle, cell, num):
    for b in range(len(Puzzle)):
        if Puzzle[b][cell[1]] == num and (b, cell[1]) != cell:
            return False


# checks validity of the cell across neighbors in the box
def validBox(Puzzle, cell, num):
    startX = cell[0] - cell[0] % 3
    startY = cell[1] - cell[1] % 3

    for x in range(startX, startX + 3):
        for y in range(startY, startY + 3):
            if Puzzle[x][y] == num and (x,y) != cell:
                return False


# condensed validRow, validCol, and validBox
'''
Couldn't run validRow, validCol, and validBox within validNum. Calls to the function either return None or False.
Using if statement with the function would end validNum early.
'''
def validNum(Puzzle, cell, num):
    for a in range(len(Puzzle)):
        if Puzzle[cell[0]][a] == num and (cell[0], a) != cell:
            return False

    for b in range(len(Puzzle)):
        if Puzzle[b][cell[1]] == num and (b, cell[1]) != cell:
            return False

    startX = cell[0] - cell[0] % 3
    startY = cell[1] - cell[1] % 3

    for x in range(startX, startX + 3):
        for y in range(startY, startY + 3):
            if Puzzle[x][y] == num and (x, y) != cell:
                return False


# checks validity of number in cell by comparing across row, column, and box
# def validNum(Puzzle, num, pos):
#     for x in range(len(Puzzle[0])):  # checks validity across all cells in row
#         if Puzzle[pos[0]][x] == num and pos[1] != x:
#             return False
#     for y in range(len(Puzzle)):  #checks validity across all cells in column
#         if Puzzle[y][pos[1]] == num and pos[0] != y:
#             return False

#     box_x = pos[1] // 3   # determines which box horizontally
#     box_y = pos[0] // 3   # determines which box vertically
#
#     for i in range(box_y*3, box_y*3 + 3):  # checks validity across all cells in box
#         for j in range(box_x * 3, box_x*3 + 3):
#             if Puzzle[i][j] == num and (i,j) != pos:
#                 return False


# def isEmpty(Puzzle):
#     for x in range(len(Puzzle)):
#         for y in range(len(Puzzle[x])):
#             if Puzzle[x][y] == 0:
#                 return True  # row, column


# def solve(Puzzle):
#     empty = isEmpty(Puzzle)
#     if not empty:
#         return True
#     else:
#         row, col = empty
#     for i in range(1,10):
#         if emptyMatrix(Puzzle):
#             Puzzle[row][col] = i
#             if solve(Puzzle):
#                 return True
#             Puzzle[row][col] = 0
#
#     return False


#
#     return True