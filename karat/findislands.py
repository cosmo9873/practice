class Solution():
    def findIslands(self,grid):
        def dfs(grid, x,y):
            height=len(grid)
            width=len(grid[0])
            if x<0 or x>=height or y<0 or y>=width or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            dfs(grid,x+1,y)
            dfs(grid,x-1,y)
            dfs(grid,x,y+1)
            dfs(grid,x,y-1)
            
        numIsland=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numIsland+=1
                    dfs(grid,i,j)
                  
                    
        print(numIsland)
            


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","1"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

a=Solution()
a.findIslands(grid)