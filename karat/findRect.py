class Solution:
    def findRect(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    x,y=i,j
                    break
            else:
                continue
            break

        width=m-x
        height=n-y
        for i in range(x,m):
            if matrix[i][y] == "1":
                width=i-x
                break

        for _ in range(y,n):
            #print(x,_)
            if matrix[x][_] == "1":
                height=_-y
                break
        print(x,y, width,height)
                    
        


matrix = [["1","0","0","0","0"],["1","0","0","1","1"],["1","0","0","1","1"],["1","1","1","1","1"]]
matrix = [["1","1","1","1","1"],["1","1","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]]
a=Solution()
a.findRect(matrix)