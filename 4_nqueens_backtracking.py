def printsolution(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def isSafe(board,r,c,n):
    for i in range(c):
        if board[r][i] == 1:
            return False
    
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        if board[i][j] == 1:
            return False
    
    for i,j in zip(range(r,n,1),range(c,-1,-1)):
        if board[i][j] == 1:
            return False
    return True

def placeQueen(board, col,n):
    if col>=n:
        return True

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if placeQueen(board, col+1, n):
                return True
            board[i][col] = 0
    return False

n = int(input("Enter no of rows/columns: "))
board = [[0 for i in range(n)] for i in range(n)]

if placeQueen(board, 0, n):
    printsolution(board, n)
else:
    print("No possible solution!")