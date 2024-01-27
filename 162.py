class Solution:
    def is_peak(self, index,l , nums):
        if index==0:
            if nums[0]>nums[1]:
                return True
            return False
        elif index==l-1:
            if nums[index]>nums[index-1]:
                return True
            return False
        else:
            if (nums[index]>nums[index-1] and nums[index]>nums[index+1]):
                return True
            return False
    def findPeakElement(self, nums):
        left, right=0, len(nums)
        if len(nums)==1:
            return 0
        while left<right:
            mid=(left+right)//2
            
            if self.is_peak(mid, len(nums), nums):
                return mid
            if nums[mid]<nums[mid-1]:#下行
                right=mid
            else:
                left=mid+1
        return left
nums=[3,1,2]
print(Solution().findPeakElement(nums))                   
