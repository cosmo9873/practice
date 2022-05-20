# https://leetcode.com/problems/maximal-rectangle/

class Solution():
    def leetcode84(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea
        
    def maximalRectangle(self, matrix):
        temp=[0]*len(matrix[0])
        maxarea=0

        for i in range(len(matrix)):
            for j in range(len(temp)):
                if matrix[i][j] == '1':
                    temp[j]+=1
                else:
                    temp[j]=0

            maxarea=max(maxarea, self.leetcode84(temp))

        return maxarea


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

a=Solution()
print(a.maximalRectangle(matrix))
