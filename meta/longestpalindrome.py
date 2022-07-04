class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        count=0
        res=""
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            return False
        
        length=len(s)   
            
        if isPalindrome(s) or length==1:
            res=s
            count=len(res)
    
        if isPalindrome(s[0:length-1]):
            temp=s[0:length-1]
        else:
            temp=self.longestPalindrome(s[0:length-1])  
        
        if len(temp)>count:
            res=temp
            count=len(temp)

        if isPalindrome(s[1:length]):
            temp=s[1:length]
        else:
            temp=self.longestPalindrome(s[1:length])
            
        if len(temp)>count:
                res=temp
                count=len(temp)

        return res

        

s="babadababsd"
s1 = "cdbbdc"
a=Solution()
print(a.longestPalindrome(s1))