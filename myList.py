class myList:
    def __init__(self, array):
        self.array=array

    def reverse(self):

        newlist=[]
        index=len(self.array)
        while index>0:
            newlist.append(self.array[index-1])
            index=index-1

        return newlist
    
    def reverse2(self):

        index=len(self.array)
        i=0
        #while i<index/2:
        for i in range(0, int(index/2)):
            self.array[i], self.array[index-1-i]=self.array[index-1-i], self.array[i]
        #   i=i+1


    def shuffle(self, n):
        newlist=[]
        index=len(self.array)

        if n>index/2:
           raise "out of bound"

        i=0
        while i<n:
           newlist.append(self.array[i])
           newlist.append(self.array[i+n])
           i = i + 1
           
        return newlist



line=[10, 100, 32, 48, 7, 62, 11, 29]

mylist=myList(line)

print(f'Original --- {mylist.array}')

print(f'reverse --- {mylist.reverse()}')

print(f'shuffle --- {mylist.shuffle(4)}')

mylist.reverse2()

print(f'reverse2 --- {mylist.array}')

#print(min(mylist.array[0:2]))

for i in range(len(mylist.array)-1, -1, -1):
    print(mylist.array[i])
