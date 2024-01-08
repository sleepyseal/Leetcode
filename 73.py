class Solution:
    def setZeroes(self, matrix):
        row_set=set()
        column_set=set()
        m, n= len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_set.add(i)
                    column_set.add(j)
        for i in row_set:
            matrix[i]=[0]*n
        for j in column_set:
            for k in range(m):
                matrix[k][j]=0
        return matrix