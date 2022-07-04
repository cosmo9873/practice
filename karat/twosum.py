#https://leetcode.com/problems/two-sum/

class Twosum:
    # def twosum(self, nums, k):
    #     hashmap={}
    #     for i in range (len(nums)):
    #         complement=k-nums[i]
    #         if complement in hashmap:
    #             return [hashmap[complement]+1, i+1]
    #         hashmap[nums[i]]=i

    def twosum(self, nums, k):
        record=set()
        for i in range (len(nums)):
            complement=k-nums[i]
            if complement in record:
                return [nums[i], complement]
            record.add(nums[i])
        return []

    # def twosum(self, nums, k):
    #     for i in range (len(nums)):
    #         complement=k-nums[i]
    #         if complement in nums:
    #             return [nums[i], complement]
    #     return []

    def twosum1(self, nums, k):
        list=[]
        n=len(nums)
        for i in range (0,n):
            for j in range (i+1, n):
                if nums[i] + nums[j] == k:
                    return [i,j]
        return []




nums = [2,8,11,15,3,4,5,6]
# nums=[-1, 0]
target = 9

a=Twosum()
print(a.twosum(nums,target))