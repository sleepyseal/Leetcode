class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum, win=0, 200000
        left, right=0, 0
        sum=0
        while(right<len(nums)):
            sum=sum+nums[right]
            while(sum>=target):
                win=min(win, right-left+1)
                if win==1:
                    return 1
                sum=sum-nums[left]
                left=left+1
            right=right+1
        if win==200000:
            return 0
        return win
s=Solution()
target = 4
nums =[1,4,4]

print(s.minSubArrayLen(target,nums))