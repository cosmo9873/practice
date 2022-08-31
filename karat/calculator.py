
# https://leetcode.com/problems/basic-calculator/
class Solution():
    def calculator(self,exp):
        
        result=0
        operand=0
        stack=[]
        sign=1
        
        for i in exp:
            if i.isnumeric():
                operand=operand*10+int(i)
            elif i == "+":
                result=result+sign*operand
                sign=1
                operand=0
            elif i == "-":
                result=result+sign*operand
                operand=0
                sign=-1
            elif i == "(":
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            elif i == ")":
                result=result+sign*operand
                result=result*stack.pop()+stack.pop()
                operand=0
                
        return (result+sign*operand)
                    

exp="100+2+3-99+87"
exp2="2+((8+3)+(3-999))"
exp3='22+8+3+3-999'
a=Solution()
print(a.calculator(exp3))