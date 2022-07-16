class Solution:
    def gloatLatin(self, s):
        res=""
        list=s.split(" ")
        vows=['a','e','i','o','u', 'A','E','I','O','U']
        for i in range(len(list)):
            if list[i][0] in vows:
                word=list[i]+'ma'
            else:
                word=list[i][1:]+list[i][0]+'ma'


            for j in range(1,i+2):
                word=word+'a'
            
            res=res+word+" "

        
        # print(res.strip())
        return res.strip()
    





sentence = "I speak Goat Latin"
# sentence = "The quick brown fox jumped over the lazy dog"
a=Solution()
print(a.gloatLatin(sentence))