

# https://leetcode.com/problems/merge-intervals/


class Solution():
    # def mergeIntervals(self, intervals):
    #     # intervals.sort(key=lambda x: x[0])
    #     intervals.sort()
    #     result=[]
    #     result.append(intervals[0])
    #     # print(result)
    #     for i in range(1,len(intervals)):
    #         temp=result[-1]
    #         # print('temp',temp)
    #         if temp[1] >= intervals[i][0]:
    #             temp[1]=intervals[i][1] if temp[1] < intervals[i][1] else temp[1]
    #             result.pop()
    #         else:
    #             temp=intervals[i]

    #         result.append(temp)
    #     print(result)

    def mergeIntervals(self,intervals):
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1]=max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])

        print(result)





intervals=[[2,6],[1,3],[8,10],[15,18], [16,19],[20,21]]
intervals2=[[1,4],[4,5]]
a=Solution()
a.mergeIntervals(intervals2)