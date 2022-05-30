class Solution:
  def addSpace(self,str,sp):
    # y=""
    # k=0
    # for i in sp:
    #     y=y+str[k:i]+" "
    #     k=i
    # return y+str[k:]

    l=list(str)
    for i in range(len(sp)):
        l.insert(i+sp[i], " ")
    return("".join(l))

    # l=list(str)
    # for i in reversed(sp):
    #     l.insert(i, " ")
    # return("".join(l))
    
    # for i in range(len(sp)):
    #     if i == 0:
    #         l=str[0:sp[i]]
    #     else:
    #         l=l+" "+str[sp[i-1]:sp[i]]
    # l=l+" "+str[sp[-1]:len(str)]

    # return(l)


s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
# s = "icodeinpython"
# spaces = [1,5,7,9]
s = "spacing"
spaces = [0,1,2,3,4,5,6]
a=Solution()
print(a.addSpace(s, spaces))