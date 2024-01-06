class Solution:
    def findLengthOfLCIS(self, nums):
        l=len(nums)
        dp=[1]*l
        ans=1
        for i in range(1, l):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
                if dp[i]>ans:
                    ans=dp[i]
            else:
                dp[i]=1
        return ans