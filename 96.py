class Solution:
    def numTrees(self, n) :
        n=n+1
        dp=[0]*n
        dp[0]=1
        dp[1]=1

        for i in range(2, n):
            for j in range(i):
                dp[i]=dp[i]+dp[j]*dp[i-j-1]
        print(dp[-1])
n=4
print(Solution().numTrees(n))