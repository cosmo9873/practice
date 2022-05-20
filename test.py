# x=1
# y=2
# a=str(x)
# # print (x, y, a)
# # print(type(x), type(a), a)


# # list=[1,2,3,4, 4,"adsb"]
# # list2=list.copy()
# # list.pop(2)
# # print(list, list2)



# # list.insert(2, "test")

# # print(myyyyylist)




# # person = {
# #     'last': 'xie',
# #     'first': 'Sean'
# # }

# # print(person)

# # person2=person.copy()
# # print(person2)

# # person['first']='Xi'
# # person.pop('first')


# # print(person)
# # print(person2)

# # def sayHello(name):
# #     print(f'Hello {name}')

# # sayHello('sean')

# # def getSum(num1, num2):
# #     return num1+num2

# # print(getSum(23, 2))

# # from camelcase import CamelCase

# # c = CamelCase()
# # print(c.hump("sean xie"))

# line="10 100 32 48 7 62 11 29"

# print(''.join(reversed(line)))

# mylist=line.split(" ")
# print(mylist)

# mylist = [int(i) for i in mylist]
# print(mylist)
import operator
import decimal

decimal.getcontext().prec = 150
e_from_decimal = decimal.Decimal(1).exp().to_eng_string()[2:]
for i in range(len(e_from_decimal)-10):
    x = int(reduce(operator.add,e_from_decimal[i:i+10]))
    if isprime(x):
        print (x)
        print (i)
        break  
