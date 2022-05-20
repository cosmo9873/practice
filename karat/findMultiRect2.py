class Solution:
    def findRect(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        orig=[]
        result=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0' and matrix[i-1][j] == '1' and matrix[i][j-1] == '1':
                    orig.append([i,j])
  
        for each in orig:
            x,y=each[0], each[1]
            width=m-x
            height=n-y

            for i in range(x,m):
                if matrix[i][y] == "1":
                    width=i-x
                    break

            for _ in range(y,n):
                if matrix[x][_] == "1":
                    height=_-y
                    break
          
            result.append([x,y,width,height])
        print(result)
                

matrix = [["1","1","1","1","1"],["1","0","0","1","1"],["1","0","0","1","1"],["1","1","1","1","1"]]
matrix = [["1","0","1","1","1"],["1","0","1","1","1"],["1","1","1","0","1"],["1","1","0","1","1"]]
a=Solution()
a.findRect(matrix)