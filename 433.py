class Solution:
    def minMutation(self, startGene, endGene, bank):
        if endGene not in bank:
            return -1
        graph={}
        def distance_is_1(g1, g2):
            d=0
            for i in range(8):
                if g1[i]!=g2[i]:
                    d+=1
                    if d>1:
                        return False
            if d==1:
                return True
            return False
        def bfs(node, graph, target, ans):
            if node==target:
                return 0
            q=[node]
            child=[]
            visited=[]
            while q:
                while q:
                    ele=q.pop(0)
                    if ele==target:
                        return ans
                    if ele not in visited:
                        visited.append(ele)
                        for i in graph[ele]:
                            if i not in visited:
                                child.append(i)
                ans+=1
                q=child
                child=[]
            return -1

        if startGene not in bank:
            bank.append(startGene)
        l=len(bank)
        for i in range(l):
            for j in range(l):
                if j!=i:
                    if distance_is_1(bank[i], bank[j]):
                        if bank[i] in graph:
                            graph[bank[i]].append(bank[j])
                        else:
                            graph[bank[i]]=[bank[j]]
        res=bfs(startGene, graph, endGene, 0)
        return res
