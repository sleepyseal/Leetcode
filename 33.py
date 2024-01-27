class Solution:
    def search(self, nums, target):
        left, right=0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]==target:
                return target
            if nums[right]==target:
                return right
            if nums[mid]>nums[left]:
                if nums[mid]>target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return -1
nums=[4,5,6,7,0,1,2]
print(Solution().search(nums, 0))