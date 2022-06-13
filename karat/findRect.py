class Solution():
    def findRect(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print(i,j)
                if matrix[i][j] == "0" and (matrix[i-1][j] != "0" or i == 0) and ( matrix[i][j-1] != "0" or j==0):
                    x,y=i,j
                    break
            else:
                continue
                
        print(x,y)
        w=1
        h=1
        for i in range(x+1, len(matrix)):
            if matrix[i][y] == "0":
                h+=1
            else:
                break

                
        for j in range(y+1, len(matrix[0])):
            if matrix[x][j] == "0":
                w+=1
            else:
                break
                
        print(w,h)
        


matrix = [["1","0","0","0","0"],
          ["1","0","0","1","1"],
          ["1","0","0","1","1"],
          ["1","1","1","1","1"]]

# matrix = [["1","1","1","1","1"],
#           ["1","1","0","0","0"],
#           ["1","1","1","1","1"],
#           ["1","1","1","1","1"]]
a=Solution()
a.findRect(matrix)