class Solution:
    def maxSubarraySumCircular(self, nums):
        # 1 2 1,-2,3,-2
        dp=[0]*len(nums)
        pre_max=[0]*len(nums)
        pre_sum=[0]*len(nums)
        post_sum=[0]*len(nums)
        post_sum[-1]=nums[-1]
        cir_val=[0]*len(nums)
        val_max=nums[0]
        dp[0]=nums[0]
        pre_sum[0]=nums[0]
        pre_max[0]=nums[0]
        cir_val[0]=sum(nums)
        for i in range(1, len(nums)):
            dp[i]=max(nums[i], nums[i]+dp[i-1])
            pre_sum[i]=nums[i]+pre_sum[i-1]
            post_sum[len(nums)-i-1]=post_sum[len(nums)-i]+nums[len(nums)-1-i]
            if pre_sum[i]>val_max:
                pre_max[i]=pre_sum[i]
                val_max=pre_sum[i]
            else:
                pre_max[i]=val_max
        ans=nums[0]
        for i in range(1, len(nums)):
            cir_val[i]=pre_max[i-1]+post_sum[i]
            ans=max(ans, cir_val[i], dp[i])
        return ans
nums=[1,-2,3,-2]
print(Solution().maxSubarraySumCircular(nums))