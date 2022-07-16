
def runLengthEncode(input: str) -> str:

    #check for empty string
    if input == "":
        return ""
    
    prev=None
    count=0
    output=""

    # iterate through the string char by char
    for c in input:
        if c == prev:
            count+=1
        else:
            if prev != None:
                output=output+str(count)+prev
            prev=c
            count=1

    #append the last segment of the encoding
    output=output+str(count)+prev
    
    return output




str1="aaaabbbbcccc"
str2="abcd"
str3="aaabbbcca"
str4=""

print(runLengthEncode(str1))
print(runLengthEncode(str2))
print(runLengthEncode(str3))
print(runLengthEncode(str4))