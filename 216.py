class Solution:
    def combinationSum3(self, k, n):
        def backtracking(k, n, start_index, path, ans):
            if len(path)==k:
                if sum(path)==n:
                    ans.append(path.copy())
                return
            for i in range(start_index, n+1-sum(path)):
                path.append(i)
                backtracking(k,n, i+1, path, ans)
                path.pop()
        ans=[]
        path=[]
        backtracking(k, n, 1, path, ans)
        return ans
