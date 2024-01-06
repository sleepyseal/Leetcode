class Solution:
    def integerBreak(self, n):
        dp=[0]*(n+1)
        dp[0], dp[1]=1, 1
        for i in range(1, n+1):
            for j in range(1, i):
                dp[i]=max(dp[i],(i-j)*j, j*dp[i-j])
        return dp[-1]

n=10
print(Solution().integerBreak( n))