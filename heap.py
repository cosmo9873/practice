import heapq

# H = [[21,1],1,45,78,3,5]
# # Create the heap

# print(H)

# heapq.heapify(H)
# print(H)

# # Replace an element
# heapq.heapreplace(H,6)
# print(H)

# print(heapq.heappop(H))
# print(H)
# heapq.heappush(H,1000)
# print(H[::-1])


count = {
    'sean': 90,
    'John': 100,
    'ted': 98,
    'zara': 23,
    'xi': 330,
    'person1': 300,
    'person2': 241,
    'person3': 130,
    'person4': 370,
    'person5': 20,
    'person6': 21,
    'person7': 17,
    'person8': 30,
    'person9': 20,
    'pern1': 415,
    'pern2': 201,
    'per3': 415,
    'per4': 330,
    'per5': 200,
    'per6': 201,
    'per7': 100,
    'per8': 320,
    'per9': 230
}

print(count)

newcount={}
for i in count:
    #print(i, count[i])
    if count[i] in newcount:
        #print('found')
        newcount[count[i]]+=[i]
    else:
        newcount[count[i]]=[i]

# for i in newcount:
#     print(i, newcount[i])

H=[]
k=6
min=0
for i in newcount:
    if i not in H:
        if len(H)<k:
          heapq.heappush(H, i)
          min=i
        elif len(H)==k:
          if i > min:
            heapq.heapreplace(H, i)
            min=i


print(H)

print('starting--------')

for i in range(len(H)-1, -1, -1):
    print(H[i], newcount[H[i]])
        
#print(H)
