# 给一个二维matrix，-1代表墙，0代表路。问给定一个起点坐标为0，是否能到达所有的0。

class Solution():
    def findLegalDFS(self,matrix,i,j):
        visited = [[ 0 for _ in range(len(matrix[0])) ] for _ in range(len(matrix))]

        
        def floodFillDFS(x,y):
            # print('flag0',x,y,len(matrix))
            if x < 0 or x >=len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y]==-1 or visited[x][y]:
                return
            # print('flag1')
            visited[x][y]=True
            floodFillDFS(x-1,y)
            floodFillDFS(x+1,y)
            floodFillDFS(x,y-1)
            floodFillDFS(x,y+1)
            # print(visited)
            
        floodFillDFS(i,j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not visited[i][j] and matrix[i][j] == 0:
                    return False

        return True

matrix=[
    [  0,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, -1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  -1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ]
    ]
a=Solution()
print(a.findLegalDFS(matrix,0,1))