class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        graph={}
        def distance_is_1(g1, g2, l):
            d=0
            for i in range(l):
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
                        if ele in graph:
                            for i in graph[ele]:
                                if i not in visited:
                                    child.append(i)
                ans+=1
                q=child
                child=[]
            return 0

        if beginWord not in wordList:
            wordList.insert(0, beginWord)
        l=len(wordList)
        word_l=len(beginWord)
        for i in range(l):
            for j in range(l):
                if j!=i:
                    if distance_is_1(wordList[i], wordList[j], word_l):
                        if i in graph:
                            graph[i].append(j)
                        else:
                            graph[i]=[j]
        end_index=wordList.index(endWord)
        start_index=wordList.index(beginWord)
        res=bfs(start_index, graph, end_index, 1)
        return res

beginWord="hit"
endWord ="cog"
wordList =["hot","cog","dot","dog","hit","lot","log"]
print(Solution().ladderLength(beginWord, endWord, wordList))