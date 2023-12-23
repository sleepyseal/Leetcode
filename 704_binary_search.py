class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right= 0, len(nums)
        while(left<right):
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return -1

s=Solution()
nums = [-1,0,3,5,9,12]
target=9
print(s.search(nums, target))           