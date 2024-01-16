class Solution:
    def solve(self, board):
        def dfs(board, i, j ,m, n):
            if board[i][j]=='O':
                board[i][j]='K'
                if i+1<m:
                    dfs(board, i+1, j, m, n)
                if i-1>-1:
                    dfs(board, i-1, j, m, n)
                if j+1<n:
                    dfs(board, i, j+1, m, n)
                if j-1>-1:
                    dfs(board, i, j-1, m, n)
        m, n=len(board), len(board[0])
        for i in range(m):
            dfs(board, i, 0, m, n)
            dfs(board, i, n-1, m, n)
        for j in range(n):
            dfs(board, 0, j, m, n)
            dfs(board, m-1, j, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j]!='K':
                    board[i][j]='X'
                elif board[i][j]=='K':
                    board[i][j]='O'
        return board
                