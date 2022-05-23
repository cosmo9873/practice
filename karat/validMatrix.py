# https://www.jianshu.com/p/fdbcba5fe5bc
# 给一个N*N的矩阵，判定是否是有效的矩阵。有效矩阵的定义是每一行或者每一列的数字都必须正好是1到N的数。输出一个bool。

class Solution():
    def isValidMatrix(self, matrix):
        for i in range(len(matrix)):
            #print('row', matrix[i])
            if self.isValidVect(matrix[i]) == False:
                return False

        for j in range(len(matrix)):
            #print('col',[sub[j] for sub in matrix])
            if self.isValidVect([sub[j] for sub in matrix]) == False:
                return False
        
        return True
  

    def isValidVect(self,vect):
        map=[0]*len(vect)
        for i in vect:
            if 1<=i<=len(vect):
                map[i-1]=1
                #print('flag2', map)
            else:
                return False
        
    
        #print('flag0',map)
        if 0 in map:
            return False
        else:
            return True



m1=[[1,3,2],[2,1,3],[3,2,1]]
m2=[[1,2,3],[1,2,3],[1,2,3]]
m3=[[1000,2,0],[-1000,2,3],[1,2,3]]

a=Solution()
print(a.isValidMatrix(m3))