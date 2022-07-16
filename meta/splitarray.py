def splitArray(array):
        left=0
        right=len(array)-1
        lsum=array[0]
        rsum=array[-1]

        while left < right-1:
            if lsum < rsum:
                left+=1
                lsum=lsum+array[left]
            else:
                right-=1
                rsum=rsum+array[right]

        if lsum==rsum:
            return left
        else:
            return -1

def printSplit(self,Array, n):
        if n == -1:
            print("Not Possible")
        else:
            print(Array[0:n+1])
            print(Array[n+1:])


Arr=[1, 2, 3, 4, 5, 5]
Arr2=[4, 1, 2, 3]
Arr3=[4, 3, 2, 1]
a=Solution()
pointer=a.splitArray(Arr3)
a.printSplit(Arr3, pointer)


