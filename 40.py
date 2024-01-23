class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        def backtracking(candidates, target, start_index, path, ans):
            if sum(path)==target:
                ans.append(path.copy())
                return
            if sum(path)>target:
                return
            ele=-1
            for i in range(start_index, len(candidates)):
                if candidates[i]!=ele:
                    path.append(candidates[i])
                    backtracking(candidates, target, i+1, path, ans)
                    ele=path.pop()
                
        path, ans=[],[]
        backtracking(candidates, target, 0, path, ans)
        return ans
candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))