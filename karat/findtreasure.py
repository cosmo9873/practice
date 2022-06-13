
class Solution():
    def findAllTreasure(self,board,start,end):
        numTreasure=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1:
                    numTreasure+=1

        print(numTreasure)
        paths=[]


        def dfs(x,y,path,remainTreasure):
            if x<0 or x >= len(board) or y<0 or y>=len(board[0]) or board[x][y] == -1 or board[x][y] == 2:
                return
            path.append([x,y])
            temp=board[x][y]
            if temp ==1:
                remainTreasure-=1
            if x == end[0] and y == end[1] and remainTreasure == 0:
                paths.append(path.copy())
                path.pop()
                return

            board[x][y]=2
            dfs(x+1,y,path,remainTreasure)
            dfs(x-1,y,path,remainTreasure)
            dfs(x,y+1,path,remainTreasure)
            dfs(x,y-1,path,remainTreasure)
            board[x][y]=temp
            path.pop()

        dfs(start[0],start[1], [], numTreasure)
        if len(paths) == 0:
            return []


        min=len(paths[0])
        list=[]
        for i in range(0,len(paths)):
            if len(paths[i]) == min:
                list.append(paths[i])
            elif len(paths[i]) < min:
                min=len(paths[i])
                list=[paths[i]]

        return list


board3 = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]
m,n=[4,3], [2,0]
m,n=[5,0], [0,4]
m,n=[5,2], [2,0]
m,n=[0,0], [4,1]

a=Solution()
for i in a.findAllTreasure(board3,m,n):
    print(i)