def searchInt(array,ascending,key,type):
    
    #ascending logic
    if ascending:

        left=0
        right=len(array)-1
        if array[0]>key:
            left=None
        elif array[-1]<key:
            right=None
            
        
        for i in range(len(array)):
            if array[i]==key:
                left=right=i
                break
            
            if array[i] < key and array[i+1]>key:
                left=i
                right=i+1
                break
        
        if type=='Equals':
            if left==right:
                return str(left), 'FoundExact'
            else: 
                return "X", 'NotFound'
                
        
        if type=='LessThan':
            if left == None:
                return 'X', 'NotFound'
            elif left==0:
                return 'X', 'NotFound'
            elif left==right:
                return left-1, 'FoundLess'
            else:
                return left, 'FoundLess'

                
        if type=='LessThanEquals':
            if left==right:
                return left, 'FoundExact'
            else: 
                return 'X', 'NotFound'
                
        if type=='GreaterThan':
            if right == None:
                return 'X', "NotFound"
            elif left==right:
                return right+1, 'FoundGreater'
            else:
                return right, 'FoundGreater'

        if type=='GreaterThanEquals':
            if left==right:
                return right, 'FoundExact'
            else: 
                return 'X', 'NotFound'
                
    # # descending, reverse logic of ascending
    # if ascending == 0:
    #     [...]

array=[0, 2, 4, 6, 8]
ascending=2

key=-1
type='LessThanEquals'
print(key, type, searchInt(array,ascending,key,type))
    

key=0
type='LessThan'
print(key, type, searchInt(array,ascending,key,type))

key=0
type='Equals'
print(key, type, searchInt(array,ascending,key,type))

key=1
type='Equals'
print(key, type, searchInt(array,ascending,key,type))

key=2
type='GreaterThanEquals'
print(key, type, searchInt(array,ascending,key,type))

key=2
type='GreaterThan'
print(key, type, searchInt(array,ascending,key,type))