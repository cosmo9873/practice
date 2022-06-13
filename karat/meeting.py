from re import M


class Solution():   
    def bookMeeting(self,MR,new):
        start_new,stop_new=new
        for start,stop in MR:
            if start<=start_new<=stop or start<=stop_new<=stop:
               return False
            else:
                return True
            




meeting_room=[[1300, 1500], [930, 1200],[830, 845]]
new=[820, 830]
new2=[1450, 1500]
a=Solution()
print(a.bookMeeting(meeting_room,new2))


