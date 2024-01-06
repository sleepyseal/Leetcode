class Solution:
    def maxProfit(self, prices):
        l=len(prices)
        dp=[]
        for i in range(l):
            dp.append([0]*2)
        dp[0][0]=-prices[0]
        for i in range(1, l):
            dp[i][0]=max(dp[i-1][0], -prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1]
    
price=[7,1,5,3,6,4]
print(Solution().maxProfit(price))