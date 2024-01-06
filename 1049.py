class Solution:
    def lastStoneWeightII(self, stones):
        s=sum(stones)
        target=s//2
        dp=[0]*(target+1)
        for i in stones:
            for j in range(target, i-1, -1):
                dp[j]=max(dp[j], dp[j-i]+i)
        return s-dp[-1]*2
stones =[2,7,4,1,8,1]
print(Solution().lastStoneWeightII(stones))