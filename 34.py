class Solution:
    def searchRange(self, nums, target):
        left, right=0, len(nums)
        index=-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                index=mid
                break
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        if index==-1:
            return [-1, -1]
        else:
            interval_left, interval_right=index, index
            if nums[0]==target:
                interval_left=0
            else:
                while interval_left>0:
                    if nums[interval_left-1]==target:
                        interval_left-=1
                    else:
                        break
            if nums[len(nums)-1]==target:
                interval_right=len(nums)-1
            else:
                while interval_right<len(nums)-2:
                    if nums[interval_right+1]==target:
                        interval_right+=1
                    else:
                        break
            return [interval_left, interval_right]
