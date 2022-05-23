from mimetypes import types_map
from zlib import Z_BEST_SPEED


class Solution:

    def find01Parent(self,pairset):
        map={}
        zeroset=[]
        oneset=[]
        # print(pairset)
        for p,c in pairset:
            if c not in map:
                map[c]=1
            else:
                map[c]+=1

            if p not in map:
                map[p]=0
        # print(map)

        for i in map:
            if map[i] == 0:
                zeroset.append(i)
            elif map[i] == 1:
                oneset.append(i)
        print(zeroset,oneset)

    def commonParent(self,pairset,n1, n2):
            pmap={}
            # print(pairset)
            for p,c in pairset:
                if c not in pmap:
                    pmap[c]={p}
                else:
                    print('flag0',c,p,pmap)
                    pmap[c].add(p)

                if p not in pmap:
                    print("flag1",c,p, pmap)
                    pmap[p]=set()


            for i in pmap:
                if pmap[i] != set():
                    seta=pmap[i].copy()
                    for p in seta:
                        for a in pmap[p]:
                            pmap[i].add(a)


            print(pmap)
            return pmap[n1].intersection(pmap[n2]) != set()
            

    def earliestParent(self,pairset,n):
            pmap={}
            # print(pairset)
            for p,c in pairset:
                if c not in pmap:
                    pmap[c]={p}
                else:
                    print('flag0',c,p,pmap)
                    pmap[c].add(p)

                if p not in pmap:
                    print("flag1",c,p, pmap)
                    pmap[p]=set()
            print(pmap)
            
            def returnEP(pmap,x,layer):
                if pmap[x] == set():
                    print('flag2',x, layer)
                    return x,layer
                else: 
                    for i in pmap[x]:
                        __depth=0
                        # print('flag3',__c,x,i,pmap[x])
                        a,b=returnEP(pmap,i,layer+1)
                        # depthmap[i]=b
                        print('flag4',a,b)
                        if b > __depth:
                            result=a
                            __depth=b
                        
                    return result, layer
            depthmap={}
            print(returnEP(pmap,n,0))

           


        
parentChildPairs = [  (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10), (11, 2) ] 
a=Solution()
# a.find01Parent(parentChildPairs)
# print(a.commonParent(parentChildPairs,1,3))
a.earliestParent(parentChildPairs,6)

