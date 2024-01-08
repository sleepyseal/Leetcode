class Solution:
    def numIslands(self, grid):
        def dfs(i, j, grid, m, n):
            grid[i][j]='0'
            if i+1<m and grid[i+1][j]=='1':
                dfs(i+1, j, grid, m,n)
            if j+1<n and grid[i][j+1]=='1':
                dfs(i, j+1, grid, m,n)
            if i-1>=0 and grid[i-1][j]=='1':
                dfs(i-1, j, grid, m,n)
            if j-1>=0 and grid[i][j-1]=='1':
                dfs(i, j-1, grid, m,n)
        m, n=len(grid), len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(i, j, grid, m, n)
        return ans
grid=[["1","1","1"],["0","1","0"],["1","1","1"]]
print(Solution().numIslands(grid))