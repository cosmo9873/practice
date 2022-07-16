
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        new=None
            
        while head:
            temp=head
            head=head.next
            temp.next=new
            new=temp

        return new



l1=ListNode(8)

temp=ListNode(7)
temp.next=l1
l1=temp
temp=ListNode(6)
temp.next=l1
l1=temp
temp=ListNode(5)
temp.next=l1
l1=temp
temp=ListNode(4)
temp.next=l1
l1=temp
temp=ListNode(3)
temp.next=l1
l1=temp
temp=ListNode(2)
temp.next=l1
l1=temp
temp=ListNode(1)
temp.next=l1
l1=temp


a=Solution()
ret=a.reverseList(l1)
while ret:
    print (ret.val)
    ret=ret.next