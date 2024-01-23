class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        def backtracking(nums, start_index, path, ans):
            ans.append(path.copy())
            if start_index>=len(nums):
                return
            used=float('inf')
            for i in range(start_index, len(nums)):
                if nums[i]!=used:
                    path.append(nums[i])
                    backtracking(nums, i+1, path, ans)
                    used=path.pop()
        path, ans=[], []
        backtracking(nums, 0, path, ans)
        return ans
nums=[1,2,2]
print(Solution().subsetsWithDup(nums))