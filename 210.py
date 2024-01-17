class Solution:
    def findOrder(self, numCourses, prerequisites):
        edge={}
        indeg=[0]*numCourses
        finish=[]
        ans=[]
        for i in prerequisites:
            indeg[i[0]]+=1
            if i[1] in edge:
                edge[i[1]].append(i[0])
            else:
                edge[i[1]]=[i[0]]
        for i in range(numCourses):
            if indeg[i]==0:
                finish.append(i)
                ans.append(i)
        while finish:
            ele=finish.pop(0)
            if ele in edge:
                for i in edge[ele]:
                    indeg[i]-=1
                    if indeg[i]==0:
                        finish.append(i)
                        ans.append(i)
        if len(ans)==numCourses:
            return ans
        return []
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))