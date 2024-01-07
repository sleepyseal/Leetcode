class Solution:
    def isValidSudoku(self, board):
        res=[]
        for i in range(27):
            res.append([])
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in res[i]:
                        return False
                    else:
                        res[i].append(board[i][j])
                    if board[i][j] in res[9+j]:
                        return False
                    else:
                        res[9+j].append(board[i][j])
                    row, column=i//3, j//3
                    if board[i][j] in res[18+row*3+column]:
                        return False
                    else:
                        res[18+row*3+column].append(board[i][j])
        return True
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))