class Solution(object):
    def row_visit(self, matrix, row, time, not_reverse):
        element_num=len(matrix[0])-1-2*time
        if not_reverse:
            return matrix[row][time: time+element_num]
        else:
            res= matrix[row][len(matrix[0])-time-element_num:len(matrix[0])-time]
            res.reverse()
            return res
    def col_visit(self, matrix, col, time, not_reverse):
        colum_num=len(matrix[0])
        row_num=len(matrix)
        element_num=row_num-1-2*time
        col_data=[r[col] for r in matrix]
        if not_reverse:
            return col_data[time: time+element_num]
        else:
            res=col_data[row_num-time-element_num:row_num-time]
            res.reverse()
            return res
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        col=len(matrix[0])
        row=len(matrix)
        if row==1:
            return matrix[0]
        if col==1:
            return [i[0] for i in matrix]
        total=col*row
        time=0
        not_reverse=True
        while(len(result)<total):
            not_reverse=True
            sq1=self.row_visit(matrix, time, time, not_reverse)
            for i in sq1:
                result.append(i)
            sq2=self.col_visit(matrix, col-time-1, time, not_reverse)
            for i in sq2:
                result.append(i)
            not_reverse=False
            sq3=self.row_visit(matrix, row-time-1, time, not_reverse)
            for i in sq3:
                result.append(i)
            sq4=self.col_visit(matrix, time, time, not_reverse)
            for i in sq4:
                result.append(i)
            if len(result)==total-1:
                result.append(matrix[row//2][col//2])
                return result
            time=time+1
        return result
        
s=Solution()
matrix=[[6,9,7]]
print(s.spiralOrder(matrix))