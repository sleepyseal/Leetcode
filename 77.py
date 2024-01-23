class Solution:
    def combine(self, n, k):
        def backtracking(n, k, start_index, path, ans):
            if len(path)==k:
                ans.append(path.copy())
                return
            for i in range(start_index, n+len(path)-k+1):
                path.append(i+1)
                backtracking(n,k, i+1, path, ans)
                path.pop()
        ans=[]
        path=[]
        backtracking(n, k, 0, path, ans)
        return ans
n = 4
k = 2
print(Solution().combine(n, k))