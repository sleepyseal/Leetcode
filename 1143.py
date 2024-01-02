class Solution:
    def longestCommonSubsequence(self, text1, text2):
        l1, l2= len(text1)+1, len(text2)+1
        dp=[]
        for i in range(l1):
            dp.append([0]*l2)

        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
text1 = "abcde"
text2 = "ace" 
print(Solution().longestCommonSubsequence(text1, text2))