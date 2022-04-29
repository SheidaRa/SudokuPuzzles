from queue import Empty
import tkinter as tk

from matplotlib.pyplot import grid

# window=tk.Tk()
# window.title(Sudoku Solver)
# window.geometry("300x200+10+20")
# window.mainloop()


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def emptyList(Puzzle):
    gridList= []
    for x in range(len(Puzzle)):
        tupleList = []
        for y in range(len(Puzzle[x])):
            if Puzzle[x][y] == 0:
                tupleList.append((x, y))
        gridList.append(tupleList)
    return gridList

def solve(Puzzle):
    find = isEmpty(Puzzle)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if emptyList(Puzzle):
            Puzzle[row][col] = i
            if solve(Puzzle):
                return True
            Puzzle[row][col] = 0

    return False

# Print the Board
def printBoard(Puzzle):
    for x in range(len(Puzzle)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - - ")

        for y in range(len(Puzzle[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(Puzzle[x][y])
            else:
                print(str(Puzzle[x][y]) + " ", end="")

def isEmpty(Puzzle):
    for x in range(len(Puzzle)):
        for y in range(len(Puzzle[x])):
            if Puzzle[x][y] == 0:
                return (x, y)  # row, colum




printBoard(board)
solve(board)
print("*******************************")
printBoard(board)


 # Checks raw and column
# def validNum(Puzzle, num, pos):
#     for x in range(len(Puzzle[0])):
#         if Puzzle[pos[0]][x] == num and pos[1] != x:
#             return False
#     for y in range(len(Puzzle)):
#         if Puzzle[y][pos[1]] == num and pos[0] != y:
#             return False
#     # Check box
#     box_x = pos[1] // 3
#     box_y = pos[0] // 3
#
#     for i in range(box_y*3, box_y*3 + 3):
#         for j in range(box_x * 3, box_x*3 + 3):
#             if Puzzle[i][j] == num and (i,j) != pos:
#                 return False
#
#     return True