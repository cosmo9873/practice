
# https://www.interviewbit.com/problems/reverse-link-list-ii/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, l1,m,n):

        if m == n: 
            return l1

        mpointer=l1
        for i in range(1,m-1):
            mpointer=mpointer.next
        
        npointer=mpointer
        for i in range(m-1,n):
            npointer=npointer.next

        temp=npointer
        npointer=npointer.next
        temp.next=None
        

        t1=mpointer.next
        new=t1
        t1=t1.next
        new.next=npointer
        print('l1',l1.val)
        print('temp',temp.val)
        while t1:
            print('flag')
            temp=t1
            t1=t1.next
            temp.next=new
            new=temp
        
        mpointer.next=new
        return l1



l1=ListNode(3)

temp=ListNode(2)
temp.next=l1
l1=temp
temp=ListNode(1)
temp.next=l1
l1=temp
# temp=ListNode(5)
# temp.next=l1
# l1=temp
# temp=ListNode(4)
# temp.next=l1
# l1=temp
# temp=ListNode(3)
# temp.next=l1
# l1=temp
# temp=ListNode(2)
# temp.next=l1
# l1=temp
# temp=ListNode(1)
# temp.next=l1
# l1=temp


m=2
n=3

a=Solution()
ret=a.reverse(l1,m,n)
while ret:
    print (ret.val)
    ret=ret.next


 



