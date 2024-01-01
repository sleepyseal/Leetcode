class Solution:
    def r_great(self, nums):
        l=len(nums)
        ans=[]
        for index in range(l):
            ans.append(l-1)
        stack=[]
        for i, ele in enumerate(nums):
            if len(stack)==0 or (len(stack)>0 and ele>=nums[stack[-1]]):
                stack.append(i)
            else:
                while len(stack)>0:
                    if ele<nums[stack[-1]]:
                        index=stack.pop()
                        ans[index]=i-1
                    else:
                        break
                stack.append(i)
        return ans
    def l_great(self, nums):
        l=len(nums)
        ans=[]
        for index in range(l):
            ans.append(0)
        stack=[]
        n_c=nums.copy()
        n_c.reverse()
        for i, ele in enumerate(n_c):
            if len(stack)==0 or (len(stack)>0 and ele>=n_c[stack[-1]]):
                stack.append(i)
            else:
                while len(stack)>0:
                    if ele<n_c[stack[-1]]:
                        index=stack.pop()
                        ans[index]=l-i
                    else:
                        break
                stack.append(i)
        ans.reverse()
        return ans
    
    def largestRectangleArea(self, heights):
        r_array=self.r_great(heights)
        l_array=self.l_great(heights)
        res=0
        for i in range(len(heights)):
            res=max((1+r_array[i]-l_array[i] )*heights[i], res)
        return res
height=[1,2,3,4,5]
height.sort()
print(Solution().largestRectangleArea(height))