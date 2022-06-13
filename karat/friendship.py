

class Solution():
    def friendShip(self, employees, friends):
        fmap={}
        dmap={}
        dcount={}
        dcount2={}

        for i in employees:
            a,b,c=i.split(", ")
            fmap[a]=[]
            if c in dmap:
                dmap[a].append(c)
            else:
                dmap[a]=c
            if c in dcount:
                dcount[c]+=1
            else:
                dcount[c]=1

        for i in friends:
            a,b=i.split(", ")
            fmap[a].append(b)
            fmap[b].append(a)

        for i in dcount:
            dcount2[i]=0
        

        # print(fmap,dmap,dcount)
        for i in dmap:
            dept=dmap[i]
            for j in fmap[i]:
                if dmap[j] != dept:
                    dcount2[dept]+=1
        for i in dcount:
            print(i, dcount2[i], "of ", dcount[i])




employees = [
  "1, Bill, Engineer",
  "2, Joe, HR",
  "3, Sally, Engineer",
  "4, Richard, Business",
  "6, Tom, Engineer"
]

# Sample Output:
# Output:
# 1: 2, 3
# 2: 1
# 3: 1, 4
# 4: 3
# 6: None

friendships = [
  "1, 2",
  "1, 3",
  "3, 4"
]

friendships2 = [
  "1, 2",
  "1, 3",
  "3, 4",
  "6, 1"
]


a=Solution()
a.friendShip(employees, friendships2)