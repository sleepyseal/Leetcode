class Solution:
    def maxArea(self, height):
        l=len(height)
        left, right= 0, l-1
        res=0
        while left<right:
            res=max(res, (right-left)*min(height[left], height[right]))
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
        return res
height=[1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))