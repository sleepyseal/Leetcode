class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow, fast=0,0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow=slow+1
        return slow

s=Solution()
nums = [3,2,2,3]
val=3
print(s.removeElement(nums, val))           