class Solution:
    def findTargetSumWays(self, nums, target):
        s=sum(nums)
        target=(s+target)
        if target%2!=0:
            return 0
        target=target//2
        dp=[0]*(target+1)
        dp[0]=1
        for i in nums:
            for j in range(target, i-1, -1):
                dp[j]+=dp[j-i]
        return dp[-1]