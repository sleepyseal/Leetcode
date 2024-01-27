class Solution:
    def searchMatrix(self, matrix, target):
        m, n= len(matrix), len(matrix[0])
        left, right=0, m*n
        while left<right:
            mid=(left+right)//2
            ind_x=mid//n
            ind_y=mid%n
            if matrix[ind_x][ind_y]>target:
                right=mid
            elif matrix[ind_x][ind_y]<target:
                left=mid+1
            else:
                return True
        return False