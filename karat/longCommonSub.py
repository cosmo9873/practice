# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def lcs(self, h1,h2):
        if not h1 or not h2: return 0

        s=""

        dp = [[ 0 for _ in range(len(h2)+1) ] for _ in range(len(h1)+1)]
        # print(dp)
        for i in range (len(h1)-1, -1, -1):
            for j in range (len(h2)-1, -1, -1):
                if h1[i] == h2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                    s=(h1[i])+" "+s
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j+1])

        

        print(s)

        return dp[0][0]



h2=["3234.html", "xys.html", "7hsaa.html" ]
h1=["3234.html", "saasa.html","xys.html", "7hsaa.html" ]


# h2='abcde'
# h1='ace'
a=Solution()
print(a.lcs(h1,h2))