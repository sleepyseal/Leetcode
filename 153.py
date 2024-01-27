class Solution:
    def findMin(self, nums):
        ans=float('inf')
        left, right=0, len(nums)
        while left<right:
            mid=(left+right)//2
            ans=min(ans, nums[mid])
            if nums[mid]>nums[left]:
                ans=min(ans, nums[left])
                left=mid+1
            else:
                ans=min(ans, nums[mid])
                right=mid
        return ans