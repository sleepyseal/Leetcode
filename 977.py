class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        new_array=[0]*l
        small, big= 0, l-1
        for i in range(l-1, -1, -1):
            x1=nums[small]**2
            x2=nums[big]**2
            if x1>=x2:
                new_array[i]=x1
                small=small+1
            else:
                new_array[i]=x2
                big=big-1
        return new_array

s=Solution()
nums =[-4,-1,0,3,10]
print(s.sortedSquares(nums))