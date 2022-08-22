# Given an array of integers greater than zero, find if there is a way to
# split the array in two (without reordering any elements) such that the
# numbers before the split add up to the same sum as the numbers after the
# split. If so, print the two resulting arrays.

# In [1]: can_partition([5, 2, 3])
# Output [1]: ([5], [2, 3])
# Return [1]: True
# 
# In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1])
# Output [2]: ([2, 3, 2], [1, 1, 1, 2, 1, 1])
# Return [2]: True
# 
# In [3]: can_partition([1, 1, 3])
# Return [3]: False
# 
# In [4]: can_partition([1, 1, 3, 1])
# Return [4]: False

def splitTwo(array):
    if len(array) == 0 or len(array) == 1:
        return False

    lsum=array[0]
    rsum=array[-1]
    left=0
    right=len(array)-1

    while left < right-1:
        if lsum < rsum:
            left+=1
            lsum+=array[left]
        else:
            right-=1
            rsum+=array[right]


    if lsum == rsum:
        print(array[0:left], array[right:])
        return True
    else:
        return False


# array = [5]
# lsum = 5
# rsum = 3, 5
# left = 0
# right = 2, 1


"""
I want to monitor a value produced from a streaming app; say one of the swap columns from vmstat. If the value exceeds a given threshold T for more than X samples out of the last W samples, I’d like a message printed out.

The command should take standard input and be invoked as:

yourscript <column_number> <occurrences> <window size> <threshold value>

Example: vmstat 1 | yourscript 7 3 5 200

That means that when the value of column 7 (1-indexed) has gone over or equal to 200 for at least 3 times in the last 5 samples, “raise the alarm” (print a message and a timestamp). Once this is no longer true, “clear the alarm” (print a different message and a timestamp). While the alarm is raised, you should not print anything until it clears.

procs -----------memory-------------- ---swap-- -----io---- -system---- ------cpu-----
 r  b    swpd    free   buff    cache     si so    bi    bo    in    cs us sy id wa st
 1  0 4159576 2837032   3576 94871344    200  1   404   384     0     0  7  2 90  0  0
 1  0 4159576 2845320   3576 94871472    200  0     0     0 28217 41010  4  4 92  0  0
 2  0 4159576 2834048   3576 94871624      0  0     0     0 17261 21099  3  2 95  0  0
 1  0 4159576 2814492   3576 94872968    300  0     0  2468 19526 54519  5  3 92  0  0 <—— Raise here
 1  0 4159576 3071100   3576 94743360      0  0   264    28 10808 13075  2  1 97  0  0
 2  0 4159576 3041796   3576 94743776      0  0     0    12 13947 22004  4  2 94  0  0 <—— Clear here
"""

C,X,W,T=sys.argv

alert=False
occur=0
f.readline()
f.readline()
history=[0]*W
while line=f.readline():
    listline=line.split()
    value=listline[C]
    if value >= T:
        history.append(1)
        if len(history) >= W:
            history.pop[0]
    
    for i in range(len(history)):
        if history[i] == 1:
            occur+=1
        
    if occur >= X:
        print('alert', time.time())
        alert=True

    if occur < X and alert == True:
        print('clear alert', time.time())
        alert=False
        