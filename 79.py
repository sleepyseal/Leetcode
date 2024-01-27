class Solution:
    def exist(self, board, word):
        def dfs(board, i, j ,m, n, word, k, ans, used):
            if board[i][j]==word[k] and used[i][j] is False:
                used[i][j]=True
                # print(i, j)
                if k+1==len(word):
                    ans[0]=True
                    return
                if i+1<m and ans[0] is False:
                    dfs(board, i+1, j, m, n, word, k+1, ans, used)
                if i>0 and ans[0] is False:
                    dfs(board, i-1, j, m, n, word, k+1, ans, used)
                if j+1<n and ans[0] is False:
                    dfs(board, i, j+1, m, n, word, k+1, ans, used)
                if j>0 and ans[0] is False:
                    dfs(board, i, j-1, m, n, word, k+1, ans, used)
                used[i][j]=False
            return
        m, n=len(board), len(board[0])
        ans=[False]
        used=[]
        for i in range(m):
            used.append([False]*n)
        for i in range(m):
            for j in range(n):
                if ans[0] is False:
                    dfs(board, i, j, m, n, word, 0, ans, used)
        return ans[0]
board = [["A"]]
word = "A"
print(Solution().exist(board, word))