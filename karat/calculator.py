class Solution:
    def calculator(self, exp):
        result=0
        sign=1
        num="0"
        stack=[]
        i=0
        while i < len(exp):
            print('flag0', i, result, int(num), stack, sign)
            
            if exp[i].isnumeric():
                while i < len(exp) and exp[i].isnumeric():
                    num=num+exp[i]
                    print('flag1', i, result, int(num), stack, sign)
                    i=i+1
                i=i-1
                result=result+sign*(int(num))
                num='0'
            
            elif exp[i] == '(':
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1             
            elif exp[i] == ')':
                result=result*stack.pop()+stack.pop()
            elif exp[i] == '+':
                sign=1
            elif exp[i] == '-':
                sign=-1
            
            i=i+1

        print('flag2',i, result, int(num), stack)
        # if num != '0':
        #     result=result+sign*(int(num))

        print(result)     

exp="100+2+3-99+87"
exp2="2+((8+3)+(3-999))"
exp3='22+8+3+3-999'
a=Solution()
a.calculator(exp2)