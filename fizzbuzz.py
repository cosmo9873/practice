

class Solution:
    def fizzBuzz(self, n: int):
        
 
        l=[]
        for i in range (1, n+1):
            
            #print(i)
            if i % 3 == 0 and i % 5 == 0:
                l.append('FizzBuzz')
            elif i % 5 == 0:
                l.append('Buzz')
            elif i % 3 == 0:
                l.append('Fizz')     
            else:  
                l.append(str(i))
            
        return l


a=Solution()
print(a.fizzBuzz(15))