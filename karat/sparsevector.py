
class Solution():
    def convertSparseVector(self,v):
        res=[]
        for i in range(len(v)):
            if v[i] != 0:
                res.append([i, v[i]])



        for i, v in res:
            print("index", i, "-->", v)



v = [2, 0, 0, 0, 0,
    3, 0, 4, 0, 0,
    0, 1, 5, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 4, 0, 0,
    0, 2, 0, 0, 0,
    0, 0, 0, 3, 0,
    0, 0, 1, 0, 0,
    0, 0, 5]

a=Solution()
a.convertSparseVector(v)