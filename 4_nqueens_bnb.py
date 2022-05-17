def printsolution(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

res = []
def isSafe(board, row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if(rowLookup[row] or slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]]):
        return False
    return True

def solveNQueensUtil(board,n,col,slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if col>=n:
        return True
    
    for i in range(n):
        if isSafe(board, i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
            board[i][col] = 1
            rowLookup[i] = True
            slashCodeLookup[slashCode[i][col]] = True
            backslashCodeLookup[backslashCode[i][col]] = True

            if solveNQueensUtil(board, n, col+1, slashCode, backslashCode,rowLookup, slashCodeLookup, backslashCodeLookup):
                res.append(board.copy())
                printsolution(board, n)
            
            board[i][col] = 0
            rowLookup[i] = False
            slashCodeLookup[slashCode[i][col]] = False
            backslashCodeLookup[backslashCode[i][col]] = False

def solveNQueens():
    n = int(input("Enter number of rows/columns: "))
    board = [[0 for i in range(n)] for j in range(n)]
    slashCode = [[0 for i in range(n)] for j in range(n)]
    backslashCode = [[0 for i in range(n)] for j in range(n)]

    x = 2 * n - 1
    rowLookup = [False] * n
    slashCodeLookup = [False] *  x
    backslashCodeLookup = [False] * x

    for rr in range(n):
        for cc in range(n):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + n - 1

    if solveNQueensUtil(board, n, 0, slashCode, backslashCode,rowLookup, slashCodeLookup, backslashCodeLookup) == False:
        print("No solution possible")
        return False

    return True

solveNQueens()
print("Number of solutions: ",len(res))