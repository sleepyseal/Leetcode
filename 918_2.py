class Solution:
    def maxSubarraySumCircular(self, nums):
        dp=[]
        for i in range(2):
            dp.append([0]*len(nums))
        dp[0][0]=nums[0]
        dp[1][0]=min(0, nums[0]) #最小子数组可以是空
        s=nums[0]
        for i in range(1, len(nums)):
            dp[0][i]=max(nums[i], nums[i]+dp[0][i-1])
            dp[1][i]=min(nums[i]+dp[1][i-1], 0)
            s+=nums[i]
        max_s, min_s= max(dp[0]), min(dp[1])
        if min_s==s:
            return max_s
        return max(max_s, s-min_s)
        