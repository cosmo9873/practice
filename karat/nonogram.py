

class Solution():
    def isValidNonogram(self, matrix, row, col):


        def isValidVect(vect, meta):
            new_meta=[]
            zcount=0
            # print(vect)
            for i in vect:
                if i == 1 and zcount != 0:
                        new_meta.append(zcount) 
                        zcount=0
                if i == 0:
                    zcount+=1
            if zcount != 0:
                new_meta.append(zcount) 
            # print(meta,new_meta)
            return meta == new_meta


        # print(isValidVect([0,1,1,0], [1,1]))

        for i in range(len(matrix)):
            # print(isValidVect(matrix[i],row[i]))
            if isValidVect(matrix[i],row[i]) == False:
                return False

        
        for i in range(len(matrix[0])):
            if isValidVect([sub[i] for sub in matrix],col[i]) == False:
                return False
        
        return True


matrix1 = [[1,1,1,1],
           [0,1,1,1],
           [0,1,0,0],
           [1,1,0,1],
           [0,0,1,1]]
rows1_1    =  [[], [1], [1,2], [1], [2]]
columns1_1 =  [[2,1], [1], [2], [1]]

matrix2 = [
    [1,1],
    [0,0],
    [0,0],
    [1,0]
]
# False
rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]

a=Solution()
print(a.isValidNonogram(matrix1,rows1_1,columns1_1))
print(a.isValidNonogram(matrix2,rows2_1,columns2_1))



#"""
# A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and has to color it according to some instructions. Specifically, each cell can be either black or white, which we will represent as 0 for black and 1 for white.

# +------------+
# | 1  1  1  1 |
# | 0  1  1  1 |
# | 0  1  0  0 |
# | 1  1  0  1 |
# | 0  0  1  1 |
# +------------+

# For each row and column, the instructions give the lengths of contiguous runs of black (0) cells. For example, the instructions for one row of [ 2, 1 ] indicate that there must be a run of two black cells, followed later by another run of one black cell, and the rest of the row filled with white cells.

# These are valid solutions: [ 1, 0, 0, 1, 0 ] and [ 0, 0, 1, 1, 0 ] and also [ 0, 0, 1, 0, 1 ]
# This is not valid: [ 1, 0, 1, 0, 0 ] since the runs are not in the correct order.
# This is not valid: [ 1, 0, 0, 0, 1 ] since the two runs of 0s are not separated by 1s.

# Your job is to write a function to validate a possible solution against a set of instructions. Given a 2D matrix representing a player's solution; and instructions for each row along with additional instructions for each column; return True or False according to whether both sets of instructions match.

# Example instructions #1

# matrix1 = [[1,1,1,1],
#            [0,1,1,1],
#            [0,1,0,0],
#            [1,1,0,1],
#            [0,0,1,1]]
# rows1_1    =  [], [1], [1,2], [1], [2]
# columns1_1 =  [2,1], [1], [2], [1]
# validateNonogram(matrix1, rows1_1, columns1_1) => True

# Example solution matrix:
# matrix1 ->
#                                    row
#                 +------------+     instructions
#                 | 1  1  1  1 | <-- []
#                 | 0  1  1  1 | <-- [1]
#                 | 0  1  0  0 | <-- [1,2]
#                 | 1  1  0  1 | <-- [1]
#                 | 0  0  1  1 | <-- [2]
#                 +------------+
#                   ^  ^  ^  ^
#                   |  |  |  |
#   column       [2,1] | [2] |
#   instructions      [1]   [1]


# Example instructions #2

# (same matrix as above)
# rows1_2    =  [], [], [1], [1], [1,1]
# columns1_2 =  [2], [1], [2], [1]
# validateNonogram(matrix1, rows1_2, columns1_2) => False

# The second and third rows and the first column do not match their respective instructions.

# Example instructions #3

# matrix2 = [
# [ 1, 1 ],
# [ 0, 0 ],
# [ 0, 0 ],
# [ 1, 0 ]
# ]
# rows2_1    = [], [2], [2], [1]
# columns2_1 = [1, 1], [3]
# validateNonogram(matrix2, rows2_1, columns2_1) => False

# The black cells in the first column are not separated by white cells.

# n: number of rows in the matrix
# m: number of columns in the matrix
# """

# 作者：关辰晓
# 链接：https://www.jianshu.com/p/fdbcba5fe5bc
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。