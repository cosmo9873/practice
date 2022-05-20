#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def lcp(self, m):
    #"Given a list of pathnames, returns the longest common leading component"
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        #m.sort()
        print(list(enumerate(s1)))
        print(s1[:1])
        for i, c in enumerate(s1):
         if c != s2[i]:
            return s1[:i]
        return s1


l=["my_prefix_what_ever", "my_prefi_what_so_ever", "my_prefix_doesnt_matter"]
a=Solution()
print(a.lcp(l))