from collections import Counter

def almostEquiv(w1,w2):

    map1=Counter(w1)
    map2=Counter(w2)

    print(map1,map2)

    for i in map1:
        if abs(map1[i] - map2[i]) > 3:
            return False
        
    return True
            

word1 = "abcdeef"
word2 = "abaaacc"

# word1 = "aaaa"
# word2 = "bccb"
print(almostEquiv(word1,word2))