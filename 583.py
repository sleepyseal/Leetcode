class Solution:
    def minDistance(self, word1, word2):
        l1,l2=len(word1), len(word2)
        dp=[]
        for i in range(l1+1):
            dp.append([0]*(l2+1))
        for k in range(l1+1):
            dp[k][0]=k
        for k in range(l2+1):
            dp[0][k]=k
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]