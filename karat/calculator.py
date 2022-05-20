class Solution:
    def calculator(self, exp):
        result=0
        sign=1
        num="0"
        for i in exp:
            print('flag0',i, result, int(num))
            if i == '(' or i == ')':
                continue
            if i != '-' and i != '+':
                num=num+i
                continue
            if i == '+':
                result=result+sign*(int(num))
                sign=1
                num='0'
            if i == '-':
                result=result+sign*(int(num))
                sign=-1
                num='0'

        if num != '0':
            result=result+sign*(int(num))

        print(result)     



exp="100+2+3-99+87"
exp="2+((8+2)+(3-999))"
a=Solution()
a.calculator(exp)