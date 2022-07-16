# Write a function that takes a list of words as input, and returns 
# a list of those words bucketized by anagrams.
#
# "Anagram" definition: a word, phrase, or name formed by rearranging
# the letters of another, such as cinema, formed from iceman.
#
# Example:
# 
# anagram_buckets(word_list)
#
# Input:  ["star", "rats", "car", "arc", "arts", "stars"]
# Output:  [ ["star", "rats", "arts"], ["car", "arc"], ["stars"] ]

from collections import defaultdict  
from typing import List
    
def anagram_buckets(word_list):
        maplist=defaultdict(list)
        for word in word_list: 
            key="".join(sorted(word))
            maplist[key].append(word)
            # if key in maplist:
            #     maplist[key].append(word)
            # else:
            #     maplist[key]=[word]

        return [ j for i, j in maplist.items() ]



input = ["star", "rats", "car", "arc", "arts", "stars"]

print(anagram_buckets(input))