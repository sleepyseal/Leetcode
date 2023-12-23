class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        index=0
        for i in range(k):
            if index<len(nums) and nums[index]<0:
                nums[index]=-1*nums[index]
                index+=1
            else:
                remain=k-i
                if remain%2==0:
                    return sum(nums)
                else:
                    return sum(nums)-2*min(nums)
        return sum(nums)

nums=[-4,-2,-3]
print(Solution().largestSumAfterKNegations(nums, 4))