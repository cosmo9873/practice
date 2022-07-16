
# https://www.interviewbit.com/problems/reverse-link-list-ii/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, l1,m,n):

        if m >= n: 
            return l1

        mpointer=l1
        for i in range(0,m-2):
            mpointer=mpointer.next
        
        npointer=l1
        for i in range(0, n-1):
            npointer=npointer.next

        temp=npointer
        npointer=npointer.next
        temp.next=None

        if m != 1:
            cur=mpointer.next
        else:
            cur=mpointer
        new=npointer
        while cur:
            temp=cur
            cur=cur.next
            temp.next=new

            new=temp
        
        if m != 1:
            mpointer.next=new
        else:
            l1=new

        return l1





l1=ListNode(8)

temp=ListNode(7)
temp.next=l1
l1=temp
# temp=ListNode(6)
# temp.next=l1
# l1=temp
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


m=1
n=2

a=Solution()
ret=a.reverse(l1,m,n)
while ret:
    print (ret.val)
    ret=ret.next


 



