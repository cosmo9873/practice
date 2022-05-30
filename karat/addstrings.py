# https://leetcode.com/problems/add-strings/

class Solution():
    def addStrings(self, n1,n2):
        length=max(len(n1), len(n2))
        carry=0
        sum=0
        result=""
        for i in range(length):
            # print(n1[i],n2[i])
            if i >= len(n1):
                d1=0
            else:
                d1=n1[len(n1)-i-1]
            
            if i >= len(n2):
                d2=0
            else:
                d2=n2[len(n2)-i-1]
                
            print("digit", d1,d2)
            sum=(int(d1)+int(d2)+carry) % 10
            carry=(int(d1)+int(d2)+carry) // 10
            result=str(sum)+result
            
        return str(result)


num1 = "99"
num2 = "153"

a=Solution()
print(a.addStrings(num1, num2))