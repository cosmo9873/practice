# Input: 
# [3, 4, 5] -> 345
# [9, 4] -> 94
# Output: 
# [4, 3, 9] -> 439

def addTwo(a,b):

    res=[]
    sum=0
    carry=0
    
    while a or b:
        d1=a.pop(-1) if a else 0
        d2=b.pop(-1) if b else 0
        carry,sum=divmod(d1+d2+carry,10)
        res.insert(0,sum)

    print(res)


a=[3,4,5], [3,4],[3],[]
b=[9,4], [9],[],[]
res=[], [9],[3,9],[4,3,9]
sum=0,9,3,4,
carry=0,0,1,0

d1=5,4,3
d2=4,9,0


a=[3,4,5]
b=[9,4]

addTwo(a,b)