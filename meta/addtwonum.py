
#https://leetcode.com/problems/add-two-numbers/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        new=ListNode(0)
        tail=new
        c=0

        while l1 or l2 or c:
            val1=(l1.val if l1 else 0)
            val2=(l2.val if l2 else 0)

            c,out=divmod(val1+val2+c, 10)

            tail.next=ListNode(out)
            tail=tail.next

            l1=(l1.next if l1 else None)
            l2=(l2.next if l2 else None)


        return new.next

    def reverse(self, l1):
        new=l1
        l1=l1.next
        new.next=None
        while l1:
            print('flag')
            temp=l1
            l1=l1.next
            temp.next=new
            new=temp
        return new

    # def reverse(self, l1):
    #     new=ListNode(l1.val)
    #     l1=l1.next
    #     while l1:
    #         temp=ListNode(l1.val)
    #         temp.next=new
    #         new=temp
    #         l1=l1.next
    #     return new



l1=ListNode(3)

temp=ListNode(4)
temp.next=l1
l1=temp

temp=ListNode(2)
temp.next=l1
l1=temp


l2=ListNode(4)
temp=ListNode(6)
temp.next=l2
l2=temp
temp=ListNode(5)
temp.next=l2
l2=temp


a=Solution()
ret=a.addTwoNumbers(l1,l2)
ret=a.reverse(l1)
while ret:
    print (ret.val)
    ret=ret.next

    #     total=self.numberize(l1)+self.numberize(l2)
    #     return self.denumberize(total)
        

    # def denumberize(self, n):
    #     l=collections.deque()
    #     while n > 0:
    #         l.insert (0, n % 10)
    #         n = int (n/10)
    #     return l
 

    # def numberize(self, l):
    #     n=0
    #     factor=1
    #     while  len(l) != 0 :
    #         n+= (l.pop() % 10) * factor
    #         factor=factor*10
    #     return n


# l1 = collections.deque()
# l2 = collections.deque()

# filling deque() with elements
# l1.append(2)
# l1.append(5)
# l1.append(6)

# l2.append(3)
# l2.append(8)



