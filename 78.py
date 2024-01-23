class Solution:
    def subset(self, nums):
        def backtracking(nums, start_index, path, ans):
            # if start_index==len(nums):
            ans.append(path.copy())
                # return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(nums, i+1, path, ans)
                path.pop()
        path, ans=[], []
        backtracking(nums, 0, path, ans)
        return ans
nums=[1,2,3]
print(Solution().subset(nums))