import numpy as np

board = np.loadtxt('puzzle4.txt')

print(board)

def pos(grid, p, q, n) :
    for j in range(9) :
        if grid[p][j] == n :
            return False
    for i in range(9) :
        if grid[i][q] == n :
            return False
    a = (p//3)*3
    b = (q//3)*3
    for i in range(3) :
        for j in range(3) :
            if grid[a + i][b + j] == n :
                return False
    return True

def solver(grid) :
    for i in range(9) :
        for j in range(9) :
            if grid[i][j] == 0 :
                for n in range(1, 10) :
                    if pos(grid, i, j, n) :
                            grid[i][j] = n
                            solver(grid)
                            grid[i][j] = 0
                return
    print(np.matrix(grid))
    input("More solutons?")

solver(board)
