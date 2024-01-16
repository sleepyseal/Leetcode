class Solution:
    def calcEquation(self, equations, values, queries):
        relation={}
        ans=[]
        def dfs(node1, node2, visited, path, ans):
            if node1==node2:
                ans[0]=path
                return
            if node1 in relation:
                for i in relation[node1]:
                    if i[0] not in visited:
                        path*=i[1]
                        visited.append(i[0])
                        dfs(i[0], node2, visited, path, ans)
                        path/=i[1]

        count=0
        for i in equations:
            if i[0] not in relation:
                relation[i[0]]=[[i[1], values[count]]]
            else:
                relation[i[0]].append([i[1], values[count]])
            if i[1] not in relation:
                relation[i[1]]=[[i[0], 1/values[count]]]
            else:
                relation[i[1]].append([i[0], 1/values[count]])
            count+=1
        for i in queries:
            if i[0] not in relation :
                ans.append(-1.0)
            elif i[0]==i[1]:
                ans.append(1.0)
            else:
                res=[-1.0]
                visited=[]
                if i[0] in relation:
                    visited=[i[0]]
                    dfs(i[0], i[1], visited, 1, res)
                ans.append(res[0])

        return ans
equations = [["a","e"],["b","e"]]
values = [4.0,3.0]
queries = [["a","b"],["e","e"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))