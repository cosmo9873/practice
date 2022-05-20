# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def validate(self, input: str):

        rightHalfMapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        leftHalfMapping = {'{', '[', '('}

        stack=[]
        for i in input:
            if i in leftHalfMapping:
                stack.append(i)
            elif i not in rightHalfMapping:
                continue
            else:
             if len(stack) == 0:
                return False
             popped=stack.pop()
             if rightHalfMapping[i] != popped:
                return False

        return len(stack) == 0
    



input='(((([]()){}())){234234})'
a=Solution()
print(a.validate(input))


# input='(([]()){}(){234234})'

# stack=[]
# valid=False

# for i in input:
#     if i in leftHalfMapping:
#         stack.append(i)
#     elif i not in rightHalfMapping:
#             continue
#     else:
#         if len(stack) == 0:
#             valid=False
#             break
#         popped=stack.pop()
#         if rightHalfMapping[i] != popped:
#             valid=False
#             break

# print(f'stack is {stack}')

# if len(stack) != 0 or valid:
#     print ("invalid")
# else:
#     print ("valid")


    


