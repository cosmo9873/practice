count = {
    'sean': 90,
    'John': 100,
    'ted': 98,
    'zara': 23,
    'xi': 330,
    'person1': 200,
    'person2': 201,
    'person3': 100,
    'person4': 330
}

# print(person)

# person2=person.copy()
# print(person2)

# person['zara']=23
# print(person)

# person.pop('first')
# print(person['zara'])
# person = {value:key for key, value in person.items()}
print(count)

newcount={}
for i in count:
    print(i, count[i])
    if count[i] in newcount:
        print('found')
        newcount[count[i]]+=[i]
    else:
        newcount[count[i]]=[i]

for i in newcount:
    print(i, newcount[i])