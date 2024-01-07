class Solution:
    def numDistinct(self, s, t):
        l1, l2=len(s), len(t)
        dp=[]
        for i in range(l1+1):
            dp.append([0]*(l2+1))
        for k in dp:
            k[0]=1
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

s='babgbag'
t='bag'
print(Solution().numDistinct(s, t))