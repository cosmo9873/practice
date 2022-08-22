
#https://leetcode.com/discuss/interview-question/1162056/facebook-onsite-e4-usa/916742

def permutation(array):
    N=len(array)
    map=[False]*N


    for i in range(N):
        if array[i] >= N:
            return False

        map[array[i]]=True

    for i in map:
        if i != True:
            return False
    
    return True

# import math

# def permutation(array):
#     N=len(array)
#     for i in range(N):
#         if array[i] <0 or array[i] > N-1:
#             return False
#         else:
#             array[i] = (array[i]+1)
        
#     for i in range(N):
#         # print(i,array[i])
#         array[abs(array[i])-1]=-1*array[abs(array[i])-1]

    
#     for i in range(N):
#         if array[i] != -1*abs(array[i]):
#             return False
    
#     return True
    




array=[0, 1, 2, 3]
array2=[3, 1, 0, 2]
array3=[0, 1, 4, 3, 6]
array4=[2,1,3,1,4]

print(permutation(array))
print(permutation(array2))
print(permutation(array3))
print(permutation(array4))