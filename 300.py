class Solution:
    # def lengthOfLIS(self, nums):
    #     l=len(nums)
    #     dp=[1]*l
    #     for i in range(l):
    #         for j in range(i):
    #             if nums[i]>nums[j]:
    #                 dp[i]=max(dp[i], dp[j]+1)
    #     return max(dp)
    def lengthOfLIS(self, nums):
        ans=0
        l=len(nums)
        dp=[]
        for i in range(l):
            dp.append([1]*l)
        for i in range(l):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i][j]=max(dp[j][j]+1, dp[i][j])
                    dp[i][i]=max(dp[i][i], dp[i][j])
                    if dp[i][i]>ans:
                        ans=dp[i][i]
                else:
                    dp[i][j]=dp[j][j]
        return ans
nums=[1,2,-10,-8,-7]
print(Solution().lengthOfLIS(nums))