
#https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

class Solution:
    def topk(self, nums, k):
   
        count=Counter(nums)
        # return [ i for i, j in count.most_common(k)]
        return heapq.nlargest(k, count.keys(), key=count.get) 
               


nums = [1,1,1,2,2,5,5,3,5,5,5]
k = 2
a=Solution()
print(a.topk(nums,k))