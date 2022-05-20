# class myString:
#     def __init__(self, string):
#         self.string=string

#     def reverseT(self):

#         newstring=str()
#         index=len(self.string)
#         while index>0:
#             newstring+=self.string[index-1]
#             index=index-1

#         return newstring


# string = myString("abcdef")

# print(string.reverseT())

string=list('abcdefghijklmn')

print(str(string))

for i in range(int(len(string)/2)):
    print(string[i])
    temp=string[i]
    string[i]=string[len(string)-i-1]
    string[len(string)-i-1]=temp

print(string)