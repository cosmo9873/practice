
#https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topk(self, nums, k):
   
        c=Counter(nums)
        return [ i for i, j in c.most_common(k)]
        
        
       


nums = [1,1,1,2,2,5,5,3,5,5,5]
k = 2
a=Solution()
print(a.topk(nums,k))