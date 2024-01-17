class Solution:

    def snakesAndLadders(self, board):
        graph={}
        m,n=len(board), len(board[0])
        count=1
        for i in range(m-1,-1,-1):
            for j in range(n):
                if board[i][j]==-1:
                    graph[count]=[count+1]
                else:
                    if count+1!=board[i][j]:
                        graph[count]=[count+1, board[i][j]]
                    else:
                        graph[count]=[count+1]
                count+=1
        del graph[m*n]
        def bfs(node, graph, ans, target):
            q=[node]
            child=[]
            visited=[]
            while q:
                while q:
                    ele=q.pop(0)
                    visited.append(ele)
                    if ele==target:
                        return ans
                    for i in graph[ele]:
                        if i not in visited:
                            child.append(i)
                ans+=1
                q=child
                child=[]
            return ans
        ans=bfs(1, graph, 0, m*n)
        return ans



board = [[-1,-1],[-1,3]]
print(Solution().snakesAndLadders(board))
