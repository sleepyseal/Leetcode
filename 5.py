class Solution:
    def longestPalindrome(self, s):
        #dp[i][j] s[i:j]是否回文
        if len(s)<=1:
            return s
        dp=[]
        ans=0
        res=s[0]
        for i in range(len(s)):
            dp.append([False]*len(s))
        for i in range(len(s)):
            dp[i][i]=True
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j]=True
                        if j-i+1>ans:
                            ans=j-i+1
                            res=s[i:j+1]
                else:
                    dp[i][j]=False                      
        return res
s='ac'
print(Solution().longestPalindrome(s))