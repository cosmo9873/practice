
# # import subprocess

# def swap(array, current):
#     if current == 0:
#         print("no-op because index is 0")
#         return

#     n=int((current-1)/2)

#     if array[current] < array[n]:
#         temp=array[current]
#         array[current]=array[n]
#         array[n]=temp
#         swap(array, n)

        
# #myFile=open('test.txt', 'r')
# #line="10 100 32 48 7 62 11 30"
# #line=myFile.read(100)

# #line = os.system("cat test.txt")
# line = subprocess.check_output("cat test.txt", shell=True).decode()

# #line=out.decode()

# mylist=line.split(" ")
# mylist = [int(i) for i in mylist]
# print(mylist)

# for i in range(0, len(mylist)):
#     swap(mylist, i)

# #print(sorted(mylist))
# #mylist.sort()
# print(mylist)

# matrix=[[1,2], [3,4]]
# print(matrix[1][1])

# import http.client
# import mimetypes
# conn = http.client.HTTPSConnection("us-central1-driven-pillar-474.cloudfunctions.net")
# payload = "Sean Xie"
# headers = {
#   'Content-Type': 'text/html'
# }
# conn.request("POST", "/function-1", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

# s='hello'
# print(s.upper())

person = {
  'name': 'John Doe',
  'age': 30
}

print(person.get('name'))

