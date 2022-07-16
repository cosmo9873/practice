

def decode (input: str) -> str: 
    # check if input is empty:
    if input == "":
        raise Exception('The string is empty')
    
    ArrayChar=list(input)
    output=""
    
    #interate through input 2 chars at a time
    while ArrayChar:
        num=int(ArrayChar.pop(0))
        char=ArrayChar.pop(0)
        for i in range(num):
            output=output+char
        
    return (output)


str1='4a4b4c'
str2='1a1b1c1d'
str3='3a3b2c1a'
str4=""

print(decode(str1))
print(decode(str2))
print(decode(str3))
print(decode(str4))



