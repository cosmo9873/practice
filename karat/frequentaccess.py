#链接：https://juejin.cn/post/6844904085913600008

from collections import defaultdict

class Solution():
    def frequentAccess(self,records):
        map=defaultdict(set)
        for name,time in records:
            map[name].add(int(time))

        result=defaultdict(set)
        for name in map:
            # print('sorted',name,sorted(map[name]))
            counter=0
            init=sorted(map[name])[0]
            for i in sorted(map[name]):
                # if name not in result:
                #     init=i
                #     result[name]=set()
                # else:
                if i-init < 100:
                    result[name].add(init)
                    result[name].add(i)
                    counter=counter+1
                else:
                    continue



        # print('map',map)
        print('result',result)


badge_records =[
     ["Paul", 1355],
     ["Jennifer", 1910],
     ["John", 830],
     ["Paul", 1315],
     ["John", 835],
     ["Paul", 1405],
     ["Paul", 1630],
     ["John", 855],
     ["John", 915],
     ["John", 900],
     ["Jennifer", 1335],
     ["Jennifer", 730],
     ["John", 1630]
     ]

a=Solution()
a.frequentAccess(badge_records)