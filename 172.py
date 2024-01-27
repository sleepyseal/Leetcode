class Solution:
    def trailingZeroes(self, n):
        dp=[0]*(n+1)
        def num5_factor(n):
            ans=0
            while n%5==0:
                ans+=1
                n=n//5
            return ans
        for i in range(1, n+1):
            dp[i]=dp[i-1]+num5_factor(i)
        return dp[n]
n=100
print(Solution().trailingZeroes(n))