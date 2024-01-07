class Solution:
    def countSubstrings(self, s):
        l=len(s)
        dp=[]
        for i in range(l+1):
            dp.append([False]*(l+1))
        res=0
        for i in range(l, 0, -1):
            for j in range(i, l+1):
                if s[i-1]==s[j-1] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j]=True
                    res+=1
        return res
s='aaa'
print(Solution().countSubstrings(s))