
# 给一个word list 和最大的长度，要求把这些word用 - 串联起来，但不能超过最大的长度。

class Solution():
    def wordWrap(self,l,maxlen):
        result=[]
        bucket=""
        for i in range(len(l)):
            # print("flag0", bucket, l[i])
            if len(l[i])+len(bucket) < maxlen:
                if bucket=="":
                    bucket=bucket+l[i]
                else:
                    bucket=bucket+"-"+l[i]
                continue
            else:

                result.append(bucket)
                bucket=l[i]

        if bucket != "":
                result.append(bucket)
        print(result)



wordlist=["1p3acres", "is", "a", "good", "place", "for", "communicate"]
wordlist=["123", "45", "67", "8901234","5678", "12345", "8", "9", "0", "1", "23"]
n=15

a=Solution()
a.wordWrap(wordlist, n)