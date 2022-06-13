class Solution:
    def __init__(self, matrix):
        self.matrix=matrix
        self.m=len(matrix)
        self.n=len(matrix[0])
                    
    def findRect(self):
        list=[]

        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] == '1':
                  rect=[i,j,1,1]
                  new=self.canExpandDown(rect)
                  print("flag0", new,rect)
                  while new != rect:
                    #print(f'flag1', new,rect)
                    rect=new
                    new=self.canExpand(rect)
                    print(f'flag1', new,rect)
                  list.append(rect)
            
        print(list)

    def canExpandDown(self,__rect):
        rect=__rect.copy()
        print("rect", rect)
        for i in range(len(rect[2])):
            if matrix[i][rect[3]] == '1':
                continue
            else:
                ipointer=i-1
                break

        for j in range(len(rect[3])):
            if matrix[j][rect[2]] == '1':
                continue
            else:
                jpointer=j-1
                break

        #print(f'flag2', rect)
        
        # if rect[0]< self.m-1 and matrix[rect[0]+1][rect[1]] == '1' and rect[0]+rect[2]<self.m:
        #     rect[2]+=1

        # if rect[1]< self.n-1 and matrix[rect[0]][rect[1]+1] == '1'and rect[1]+rect[3]<self.n:
        #     rect[3]+=1
        #print(f'flag3', rect)
        return rect
                    
                  
                  

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
# for _ in matrix:
#     print(_)
a=Solution(matrix)
a.findRect()