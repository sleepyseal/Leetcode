class Solution:
    def productExceptSelf(self, nums):
        l=len(nums)
        l_array, r_array=[0]*l, [0]*l
        for i in range(l):
            if i==0:
                l_array[i]=1
            else:
                l_array[i]=nums[i-1]*l_array[i-1]
            j=l-1-i 
            if j==l-1:
                r_array[j]=1
            else:
                r_array[j]=r_array[j+1]*nums[j+1]
        res=[l_array[i]*r_array[i] for i in range(l)]
        return res
nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))