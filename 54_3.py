class Solution:
    def spiralOrder(self, matrix):
        m, n= len(matrix), len(matrix[0])
        visit=[]
        for i in range(m):
            visit.append([False]*n)
        ans=[]
        d=0
        def is_valid(i, j,m, n, visit):
            if i >=m or i<0 or j >=n or j<0 or visit[i][j]==True:
                return False
            return True
        
        def dfs(i, j , visit, matrix, ans):
            ans.append(matrix[i][j])
            visit[i][j]=True
        i, j=0,-1
        while len(ans)<m*n:
            if d%4==0:
                if is_valid(i,j+1, m,n, visit):
                    j=j+1
                else:
                    d=d+1
            elif d%4==1:
                if is_valid(i+1,j, m,n, visit):
                    i+=1
                else:
                    d=d+1
            elif d%4==2:
                if is_valid(i-1,j, m,n, visit):
                    i-=1
                else:
                    d=d+1
            elif d%4==3:
                if is_valid(i,j-1, m,n, visit):
                    j-=1
                else:
                    d=d+1
            if is_valid(i,j, m,n, visit):
                dfs(i, j, visit, matrix, ans)
        return ans
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(Solution().spiralOrder(matrix))