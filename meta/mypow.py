# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x,n):
        N=n
        if N < 0:
            x=1/x
            N=-1*N
        
        print(x,N)
        res=float(1)

        for i in range(N):
            res=float(res*x)

        return "%.5f" % res


x=2
n=-2
a=Solution()
print( a.myPow(x,n))