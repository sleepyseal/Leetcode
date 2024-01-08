class Solution:
    def gameOfLife(self, board):

        def is_valid(i, j, m, n):
            if i<m and i>=0 and j<n and j>=0:
                return True
            return False
        
        m,n =len(board), len(board[0])
        next_m=[]
        for i in range(m):
            next_m.append([0]*n)
        for i in range(m):
            for j in range(n):
                relate_coor=[[i-1, j-1],[i-1,j], [i-1,j+1], [i, j-1], [i,j+1],[i+1, j-1],[i+1,j], [i+1,j+1]]
                count_live=0
                if board[i][j]==0:
                    for index in relate_coor:
                        if is_valid(index[0], index[1], m, n):
                            if board[index[0]][index[1]]==1:
                                count_live+=1
                    if count_live==3:
                        next_m[i][j]=1
                else:
                    for index in relate_coor:
                        if is_valid(index[0], index[1], m, n):
                            if board[index[0]][index[1]]==1:
                                count_live+=1
                    if count_live<2 or count_live>3:
                        next_m[i][j]=0
                    else:
                        next_m[i][j]=1
        for i in range(m):
            board[i]=next_m[i]

        return board
board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(Solution().gameOfLife(board))
print('ok')
