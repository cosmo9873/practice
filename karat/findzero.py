class Solution():
    def findZero(self,m,x,y):
        result=[]
        for i,j in (x-1,y), (x+1,y), (x, y-1), (x,y+1):
                if m[i][j] == '0': result.append([i,j]); print (i,j)
        return result
        



matrix = [["1","0","1","0","0"],
          ["1","0","0","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
x,y=2,2

a=Solution()
print(a.findZero(matrix,x,y))