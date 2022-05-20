#https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isSudokuValid(self, board):
        N=9
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for r in range(N):
            for c in range(N):
                val=board[r][c]
                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                index=(r//3)*3+c//3
                if val in boxes[index]:
                    return False
                boxes[index].add(val)

        return True



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2=[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

a=Solution()
print(a.isSudokuValid(board2))