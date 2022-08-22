
#https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

class Solution:
    def topk(self, nums, k):
   
        count=Counter(nums)
        # return [ i for i, j in count.most_common(k)]
        # return heapq.nlargest(k, count.keys(), key=count.get) 
        # return [item_id for item_id, count in sorted(count.items(), key=lambda why:-why[1])[:k]]

        heap = []
        for item_id, count in count.items():
            heapq.heappush(heap, (count, item_id))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item_id for count, item_id in heap]
               


nums = [1,1,1,2,2,5,5,3,5,5,5]
k = 2
a=Solution()
print(a.topk(nums,k))