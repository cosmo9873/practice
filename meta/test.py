def findNumOfBattleships(board):
    count=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="X" and ((i == 0 and j==0) or (i==0 and board[i][j-1] == '.') or (j==0 and board[i-1][j]=='.') or (board[i][j-1] == '.' and board[i-1][j]=='.')):
                count+=1
    return count



board = [["X",".",".","X"],
         [".","X",".","X"],
         [".",".",".","X"]]
board2 = [["X","."],
         [".","X"]]
board3 = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", "X", ".", ".", "X", ".", ".", "."],
         [".", ".", ".", "X", "X", ".", "X", "."],
         [".", ".", "X", ".", "X", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]

print(findNumOfBattleships(board))