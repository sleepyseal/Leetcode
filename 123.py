class Solution:
    def maxProfit(self, prices):
        l=len(prices)
        dp=[]
        for i in range(4):
            dp.append([0]*l)
        dp[0][0]=-prices[0]
        dp[2][0]=-prices[0]
        for i in range(1,l):
            dp[0][i]=max(dp[0][i-1], -prices[i])
            dp[1][i]=max(dp[1][i-1], dp[0][i-1]+prices[i])
            dp[2][i]=max(dp[2][i-1], dp[1][i-1]-prices[i])
            dp[3][i]=max(dp[3][i-1], dp[2][i-1]+prices[i])
        return dp[3][-1]
p=[1,2,3,4,5]
print(Solution().maxProfit(p))