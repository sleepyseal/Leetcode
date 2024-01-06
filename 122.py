class Solution:
    def maxProfit(self, prices):
        l=len(prices)
        dp=[]
        for i in range(2):
            dp.append([0]*l)
        dp[0][0]=-prices[0]
        for i in range(1, l):
            dp[0][i]=max(dp[0][i-1], dp[1][i-1]-prices[i])
            dp[1][i]=max(dp[1][i-1], dp[0][i-1]+prices[i])
        return dp[1][-1]