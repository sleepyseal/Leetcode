class Solution:
    def permute(self, nums):
        def backtracking(nums, used, path, ans):
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            for i in range(0, len(nums)):
                if nums[i] not in used:
                    used.append(nums[i])
                    path.append(nums[i])
                    backtracking(nums, used, path, ans)
                    path.pop()
                    used.pop()
        path, ans, used=[], [], []
        backtracking(nums, used, path, ans)
        return ans

nums=[1,2,3]
print(Solution().permute(nums))