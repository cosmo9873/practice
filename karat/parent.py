from mimetypes import types_map
from zlib import Z_BEST_SPEED


class Solution:

    # def find01Parent(self,pairset):
    #     map={}
    #     zeroset=[]
    #     oneset=[]
    #     # print(pairset)
    #     for p,c in pairset:
    #         if c not in map:
    #             map[c]=1
    #         else:
    #             map[c]+=1

    #         if p not in map:
    #             map[p]=0
    #     # print(map)

    #     for i in map:
    #         if map[i] == 0:
    #             zeroset.append(i)
    #         elif map[i] == 1:
    #             oneset.append(i)
    #     print(zeroset,oneset)

    def find01Parent(self, pairs):
        pmap={}
        for p,c in pairs:
            if c not in pmap:
                pmap[c]=[p]
            else:
                pmap[c].append(p)
            if p not in pmap:
                pmap[p]=[]
        
        for i in pmap:
            if len(pmap[i]) == 0 or len(pmap[i]) == 1:
                print (i, ": ", pmap[i])

    # def commonParent(self,pairset,n1, n2):
    #         pmap={}
    #         # print(pairset)
    #         for p,c in pairset:
    #             if c not in pmap:
    #                 pmap[c]={p}
    #             else:
    #                 print('flag0',c,p,pmap)
    #                 pmap[c].add(p)

    #             if p not in pmap:
    #                 print("flag1",c,p, pmap)
    #                 pmap[p]=set()


    #         for i in pmap:
    #             if pmap[i] != set():
    #                 seta=pmap[i].copy()
    #                 for p in seta:
    #                     for a in pmap[p]:
    #                         pmap[i].add(a)


    #         print(pmap)
    #         return pmap[n1].intersection(pmap[n2]) != set()


    def commonParent(self,pairs,x,y):
        pmap={}
        for p,c in pairs:
            if c not in pmap:
                pmap[c]=[p]
            else:
                pmap[c].append(p)
            if p not in pmap:
                pmap[p]=[]
                
        print(pmap[x],pmap[y])
        
        return set(pmap[x]).intersection(pmap[y]) != set()
            

    def earliestParent(self,pairset,n):

        def returnTop(x,count):
            count+=1
            if pmap[x] == []:
                print("top",x,count)
                cmap[x]=count
            else:
                for i in pmap[x]:
                    returnTop(i,count)
        cmap={}
        count=0
        pmap={}
        for p,c in pairset:
            if c not in pmap:
                pmap[c]=[p]
            else:
                pmap[c].append(p)
            if p not in pmap:
                pmap[p]=[]

        print(pmap)
        
        returnTop(n,count)
        print(cmap)
        count=0
        for i in cmap:
            if cmap[i] > count:
                p=i
                count=cmap[i]

        print(p)

        
           


        
parentChildPairs = [  (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10), (11, 2) ] 
a=Solution()
# a.find01Parent(parentChildPairs)
# print(a.commonParent(parentChildPairs,1,3))
a.earliestParent(parentChildPairs,6)

