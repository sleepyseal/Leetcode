class Solution:
    def maxProfit(self, k, prices):
        l=len(prices)
        dp=[]
        for i in range(k*2):
            dp.append([0]*l)
        for i in range(l):
            for j in range(2*k):
                if i==0:
                    dp[j//2*2][i]=-prices[i]
                else:
                    if j==0:
                        dp[j][i]=max(dp[j][i-1], -prices[i])
                    else:
                        dp[j][i]=max(dp[j][i-1], dp[j-1][i-1]+prices[i]*(-1)**(1+j))
        return dp[-1][-1]

k = 2
prices = [3,2,6,5,0,3]
print(Solution().maxProfit(k, prices))