


from functools import lru_cache

def wordBreak(s, wordDict) -> bool:
        @lru_cache
        def helper(s,wordDict, start):
            if start == len(s):
                return True
            
            for i in range(start+1, len(s)+1):
                if s[start:i] in wordDict and helper(s,wordDict, i):
                    return True

            return False

        return helper(s, frozenset(wordDict), 0)


s = "leetcode"
wordDict = ["leet","code"]

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s,wordDict))