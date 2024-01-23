class Solution:
    def findSubsequences(self, nums):
        def backtracking(nums, start_index, used, path, ans):
            if len(path)>1 and path[-1]>=path[-2]:
                ans.append(path.copy())
            used=set()
            for i in range(start_index, len(nums)):
                if nums[i] not in used:
                    if len(path)==0 or nums[i]>=path[-1]:
                        path.append(nums[i])
                        used.add(nums[i])
                        backtracking(nums, i+1, used, path, ans)
                        path.pop()
                        # used.remove(nums[i]) 
        path, ans=[],[]
        used=set()
        backtracking(nums, 0, used, path, ans)
        return ans
nums = [4,7,5,7]
print(Solution().findSubsequences(nums))