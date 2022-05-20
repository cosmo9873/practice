def first_string ( string):
    count = {}
    for i in string:
        if i in count:
             return i
        else:
             count[i]=1
    return None

print ( "first char is ", first_string ("adbadacaba"))
