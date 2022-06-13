"""
After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['c', 'c', 't', 'n', 'a', 'x'],  
    ['c', 'c', 'a', 't', 'n', 't'],  
    ['a', 'c', 'n', 'n', 't', 't'],  
    ['t', 'n', 'i', 'i', 'p', 'p'],  
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "ant"
word5 = "aoi"
word6 = "ki"
word7 = "aaoo"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word2) =>
       [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
find_word_location(grid1, word3) => [(5, 0)]
find_word_location(grid1, word4) => [(0, 4), (1, 4), (2, 4)] OR [(0, 4), (1, 4), (1, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 2), (5, 3), (5, 4), (5, 5)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word

"""

def find_word_location(grid, word):
    
    def dfs(x,y,path,word):
        # print('flag',path,word)
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
            return
        val=grid[x][y]
        if val == word[0]:
            path.append([x,y])
            if len(word) == 1:
               return True
            if dfs(x+1,y,path,word[1:]):
                return path
            if dfs(x,y+1,path,word[1:]):
                return path
            
    for i in range(len(grid)):
        for j in range(len(grid[0])): 
            path=[]
            if dfs(i,j,path, word):
                return path
   

        
grid1 = [
    ['c', 'c', 't', 'n', 'a', 'x'],  
    ['c', 'c', 'a', 't', 'n', 't'],  
    ['a', 'c', 'n', 'n', 't', 't'],  
    ['t', 'n', 'i', 'i', 'p', 'p'],  
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "ant"
word5 = "aoi"
word6 = "ki"
word7 = "aaoo"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"


print(find_word_location(grid1, word1))
print(find_word_location(grid1, word2))
print(find_word_location(grid1, word3))
print(find_word_location(grid1, word4))
print(find_word_location(grid1, word5))
print(find_word_location(grid1, word6))
print(find_word_location(grid1, word7))
print(find_word_location(grid1, word8))
print(find_word_location(grid2, word9))




# def find_embedded_word(words, s):
#     for i in words:
#         l=list(i)
#         map={}
#         for _ in l:
#             if _ not in map:
#                 map[_]=1
#             else:
#                 map[_]+=1
    
#         for j in s:
#             if j in map:
#                 if j in map:
#                     map[j]-=1
                    
#         # print(map)
            
#         found=True
#         for _ in map:
#             if map[_] > 0:
#                 # print('flag0')
#                 found=False
#                 break
        
#         if found:
#             return i
    

# print(find_embedded_word(words, string1))
# print(find_embedded_word(words, string2))
# print(find_embedded_word(words, string3))
# print(find_embedded_word(words, string4))
# print(find_embedded_word(words, string5))
# print(find_embedded_word(words, string6))
