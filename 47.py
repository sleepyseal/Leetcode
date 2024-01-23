class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        def backtracking(nums, used, path, ans):
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            ele=float('inf')
            for i in range(0, len(nums)):
                if nums[i]!=ele and used[i] is False:
                    path.append(nums[i])
                    used[i]=True
                    backtracking(nums, used, path, ans)
                    used[i]=False
                    ele=path.pop()

        used, path, ans=[False]*len(nums), [],[]
        backtracking(nums, used, path, ans)
        return ans
nums=[3,3,0,3]
print(Solution().permuteUnique(nums))