class Solution(object):    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        up, left=0,0
        res=[]
        down, right=len(matrix)-1, len(matrix[0])-1
        while True:
            #right
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up=up+1
            if up>down:
                break
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right=right-1
            if left>right:
                break
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down=down-1
            if up>down:
                break
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left=left+1
            if left>right:
                break
        return res
s=Solution()
matrix=[[]]
print(s.spiralOrder(matrix))