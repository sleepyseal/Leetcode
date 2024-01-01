class Solution:
    def r_great(self, nums):
        ans=[-1]*len(nums)
        stack=[0]
        for i, ele in enumerate(nums):
            if len(stack)==0 or ele<=nums[stack[-1]]:
                stack.append(i)
            else:
                while stack:
                    if ele>nums[stack[-1]]:
                        index=stack.pop()
                        ans[index]=ele 
                    else:
                        break
                stack.append(i)
        return ans
    def nextGreaterElements(self, nums):
        l=len(nums)
        for i in range(len(nums)-1):
            nums.append(nums[i])
        r_array=self.r_great(nums)
        # 成环的问题都变成两倍长度取模的问题
        return r_array[:l]

nums=[5,4,3,2,1]
print(Solution().nextGreaterElements(nums))