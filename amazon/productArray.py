
def productCalc(array: list) -> list:

    # Compute total product of Array of nums
    all_product=1
    for num in array:
        all_product=all_product*num
    
    # print(all_product)
    productArray=[]
    for num in array:
        productArray.append(int(all_product/num))

    return (productArray)

def minMax(array: list) -> list:
    if array==[]:
        raise Exception("Array is empty")

    min=array[0]
    max=array[0]

    for n in array:
        if min > n:
            min=n
        if max < n:
            max = n

    return [min,max]

    




numlist=[1,2,5,34,20,23,40,204,9]
# numlist=[1,2,3]
# numlist=[]
# print(productCalc(numlist))
print(minMax(numlist))


