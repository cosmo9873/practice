# class Solution():
#     def mergeMeeting(self, intervals):
#         intervals.sort()
#         result=[]
#         result.append(intervals[0])
#         # print(result)
#         for i in range(1,len(intervals)):
#             temp=result[-1]
#             # print('temp',temp)
#             if temp[1] >= intervals[i][0]:
#                 temp[1]=intervals[i][1] if temp[1] < intervals[i][1] else temp[1]
#                 result.pop()
#             else:
#                 temp=intervals[i]

#             result.append(temp)
#         print(result)

#         result2=[]
#         for i in range(len(result)):
#             if i == 0:
#                 result2.append([0, result[i][0]])
#             if i == len(result)-1:
#                 result2.append([result[i][1],0])
#             else:
#                 result2.append([result[i][1],result[i+1][0]])

#         print(result2)

class Solution():
    def mergeMeeting(self,intervals):
        intervals.sort()
        result=[]
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1]=max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
                
         
        print([0,result[0][0]])      
        for i in range(len(result)-1):
            print([result[i][1],result[i+1][0]])
        print([result[-1][1],2359])
            
            


meeting_room=[[1100, 1500], [930, 1200],[830, 845]]
a=Solution()
a.mergeMeeting(meeting_room)



meeting_room=[[1100, 1500], [930, 1200],[830, 845]]
a=Solution()
a.mergeMeeting(meeting_room)
