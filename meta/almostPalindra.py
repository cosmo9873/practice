def almostPalindra(s):

    N=len(s)
    if N == 0 or s==None:
        return False


    left=0
    right=N-1
    while left < right:
        if s[left] != s[right]:
            if s[left] == s[right-1]:
                right-=1
                count+=1
            elif s[left+1] == s[right]:
                left+=1
                count+=1
            else:
                return False
        
        left+=1
        right-=1
    
    return True

# def isPalindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False

# def almostPalindra(s):
#     s=list(s)
#     N=len(s)
#     if N == 0 or s==None:
#         return False

#     left=0
#     right=N-1
#     while left < right:
#         if s[left] != s[right]:
#             print(s[left+1:right+1], s[left:right])
#             return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])

#         left+=1
#         right-=1

#     return True




# s = 'gfadafg'
# N = 6
# count = 0
# left = 0
# right = 5

str1="abbac" #--> return True
str2="gfadafg"  #--> return True
str3="cabbacc" #--> return True
str4="cchhhabbacc" #--> return False
str5="bcacbcab" #-->return True

print(almostPalindra(str1))
print(almostPalindra(str2))
print(almostPalindra(str3))
print(almostPalindra(str4))

print(almostPalindra(str5))