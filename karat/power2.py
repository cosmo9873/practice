# https://leetcode.com/problems/power-of-two/

import math

class Solution:
    def powerOf2(self, n: int):
        # x=math.log2 (n)
        # return x == int (x)
        while n % 2 == 0:
            n/=2
        return n == 1
        



n=78
a=Solution()
print(a.powerOf2(n))
