# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        
        h=height
        i=1
        j=len(height)-2

        lmax=0
        rmax=0

        total=0
        while i<=j:
            lmax, rmax=max(lmax, h[i]), max(rmax, h[j])
            if lmax <= rmax:
                total=total+(lmax-h[i])
                i=i+1
            elif lmax>rmax:
                total=total+(rmax-h[j])
                j=j-1

        return total


h=[0,1,0,2,1,0,1,3,2,1,2,1]

#h=[]


print(h)

a=Solution()
print(a.trap(h))

class Solution:
    def trap(self, height):
        
        res = 0
        max_left, max_right = 0, 0
        left, right = 1, len(height)-2
        while left <= right:
            max_left = max(max_left, height[left-1])
            max_right = max(max_right, height[right+1])
            if max_left <= max_right:
                if max_left > height[left]:
                          res += max_left - height[left]
                left += 1
            else:
                if max_right > height[right]:
                        res += max_right - height[right]
                right -= 1     
        return res

