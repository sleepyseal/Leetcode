class Solution:
    def rotate(self, matrix):
        l=len(matrix)
        t=l//2
        for k in range(t):
            for j in range(k, l-1-k):
                l1_value=matrix[k][j]
                l1_index=[k, j]
                l2_value=matrix[j][l-k-1]
                l2_index=[j, l-k-1]

                l3_value=matrix[l-k-1][l-1-j]
                l3_index=[l-k-1, l-1-j]
                l4_value=matrix[l-1-j][k]
                l4_index=[l-1-j, k]

                matrix[l1_index[0]][l1_index[1]]=l4_value
                matrix[l2_index[0]][l2_index[1]]=l1_value
                matrix[l3_index[0]][l3_index[1]]=l2_value
                matrix[l4_index[0]][l4_index[1]]=l3_value
        return matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(matrix))