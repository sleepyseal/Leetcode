class Solution:
    def combinationSum(self,candidates, target):
        def backtracking(candidates, target, start_index,  path, ans):
            if sum(path)==target:
                ans.append(path.copy())
                return
            if sum(path)>target:
                return
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                backtracking(candidates, target, i, path, ans)
                path.pop()
            return
        path=[]
        ans=[]
        backtracking(candidates, target,0, path, ans)
        return ans
candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))