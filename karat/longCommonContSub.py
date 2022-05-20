class Solution:
    def lcs(self, h1,h2):
        if not h1 or not h2: return 0

        s=[]
        count=-1

        dp = [[ 0 for _ in range(len(h2)+1) ] for _ in range(len(h1)+1)]
        # print(dp)
        for i in range (1,len(h1)+1):
            for j in range (1,len(h2)+1):
                if h1[i-1] == h2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    if dp[i][j] > count:
                       count=dp[i][j]
                       s=h1[i-count:i]

        print(s)

        return dp[0][0]



# h2=["3234.html", "xys.html", "7hsaa.html","asdf" ]
# h1=["3234.html", "saasa.html","xys.html", "7hsaa.html","asdf" ]


h2='abcdee'
h1='acecdecdee'
a=Solution()
print(a.lcs(h1,h2))