class Solution:
    def canPartition(self, nums):
        s=sum(nums)
        if s%2==1:
            return False
        target=s//2
        dp=[0]*(target+1)
        for i in range(len(nums)):  #遍历物品
            for j in range(target, nums[i]-1, -1):
                dp[j]=max(dp[j], dp[j-nums[i]]+nums[i])
        if dp[-1]==target:
            return True
        return False

nums = [1,5,11,5]
print(Solution().canPartition(nums))