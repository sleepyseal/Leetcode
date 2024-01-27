class Solution:
    def wordBreak(self, s, wordDict):
    #dp[i][j] 以j结尾的单词能不能用前i个单词拼出
        m, n=len(wordDict), len(s)
        dp=[]
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                word=s[i:j]
                if dp[i] and word in wordDict:
                    dp[j]=True
        # print(dp)
        return dp[-1]
s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))