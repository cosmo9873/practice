# Definition for singly-linked list.


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def reverseList(self):
        cur=self.head
        new=None
    
        while cur:
            temp=cur.next
            cur.next=new
            new=cur
            cur=temp
        ll=LinkedList()
        ll.head=new
        return ll

    def insert_bottom(self, val):

        new=Node(val, None)

        if self.head == None:
            self.head=new
            return

        i=self.head
        while i.next:
           i=i.next
        i.next=new

    def print_list(self):

        llstr=''
        i=self.head
        while i:
            llstr+=str(i.val)+'-->'
            i=i.next
        print(llstr)


ll=LinkedList()
ll.insert_bottom(1)
ll.insert_bottom(2)
ll.insert_bottom(3)
ll.insert_bottom(4)
ll.insert_bottom(5)


ll.print_list()

r=ll.reverseList()

r.print_list()

# llstr=''
# while r:
#     llstr+=str(r.val)+'-->'
#     r=r.next

# print(llstr)



