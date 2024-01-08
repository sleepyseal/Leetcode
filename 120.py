class Solution:
    def minimumTotal(self, triangle):
        #dp[i][j] i-1层 j-1节点，最小代价
        #dp[i][j]=min(dp[i-1][j-1], dp[i-1][j])+t[i][j]
        l=len(triangle)
        dp=[]
        for i in range(l):
            dp.append([0]*(l))
        dp[0][0]=triangle[0][0]
        for i in range(1, l):
            for j in range(0, i+1):
                if j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==i:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
        return min(dp[-1])
triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))