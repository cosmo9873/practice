# def fib(n):
# 	if n <= 0:
# 		raise Exception('Number must be greater than or equal to 1')
# 	elif n == 1:
# 		return 0
# 	elif n == 2:
# 		return 1
# 	else:
# 		return fib(n-1) + fib(n-2)

# def fib(n):
#     fib_array=[0,1]
#     if n == 0: 
#         raise Exception('Invalid fib number')
#     elif n ==1:
#         return 0

#     for i in range(2,n):
#         fib_array.append(fib_array[i-1]+fib_array[i-2])

    
#     print(fib_array)
#     return fib_array[n-1]

def fib(n):
    if n == 0:
        raise Expection('Invalid fib number')
    if n == 1:
        return 0

    fib1=0
    fib2=1
    for i in range(2, n):
        fib=fib1+fib2
        fib1=fib2
        fib2=fib

    print(fib)
    return fib




# print(fib(0))

# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))
print(fib(11))