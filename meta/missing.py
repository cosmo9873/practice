# def missing(nums):
#     N=len(nums)
#     map=[0]*N

#     for i in range(N):
#         if nums[i] < N:
#             map[nums[i]] = 1

#     print(map)
#     for i in range(N):
#         if map[i] == 0:
#             return i

def missing(nums):
    N=len(nums)

    for i in range(N):
        if nums[i] < N:
            nums[abs(nums[i])]*=-1

    print(nums)
    for i in range(N):
        if nums[i] > 0:
            return i


# nums=[3,0,1]
nums=[0,6,4,2,3,5,7,8,0,1]
print(missing(nums))