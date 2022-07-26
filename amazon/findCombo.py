

wordlist=['star', 'super', 'high', 'way', 'highway', 'superhighway', 'superstar']
wordlist=['star', 'super', 'high', 'way', 'superhighway', 'superstar']


def findCombo(word, wordlist):  
    if wordlist==None or word=="":
        return 

    for w in wordlist:
        if w != word and w in word:
            remainder=word.replace(w, "")
            sublist.append(w)
            print(w, remainder,sublist, wordlist)
            if remainder == "":
               print(sublist)
            findCombo(remainder, wordlist.remove(w))




for i in wordlist:
    remainder=""
    sublist=[]
    findCombo(i, wordlist)
    # if reminder=="":
    #     print(i, sublist)


    