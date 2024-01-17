# class Solution:
#     def canFinish(self, numCourses, prerequisites):
#         def create_relation(prerequisites):
#             relation={}
#             for i in prerequisites:
#                 if i[0] not in relation:
#                     relation[i[0]]=[i[1]]
#                 else:
#                     relation[i[0]].append(i[1])
#             return relation
        
#         # def dfs(relation, course, visited, ans):
#         #     if course not in relation:
#         #         return
#         #     visited.append(course)
#         #     for i in relation[course]:
#         #         if i in visited and i==visited[0]:
#         #             ans[0]=False
#         #             return
#         #         if i not in visited:
#         #             dfs(relation, i, visited, ans)
#         # ans=[True]
#         # for i in course:
#         #     visited=[]
#         #     dfs(relation, i, visited, ans)
#         # return ans[0]
#         relation=create_relation(prerequisites)
#         course=[i for i in range(numCourses)]
#         finish=[]

#         for i in course:
#             if i not in relation:
#                 finish.append(i)

#         while len(relation)>0:
#             d=[]
#             for i in relation:
#                 pre_course=relation[i]
#                 pre_course_filter=[]
#                 for j in pre_course:
#                     if j not in finish:
#                         pre_course_filter.append(j)
#                 if len(pre_course_filter)==0:
#                     finish.append(i)
#                     d.append(i)
#                 else:
#                     relation[i]=pre_course_filter

#             for k in d:
#                 del relation[k]

#             if len(d)==0:
#                 break
#         if len(relation)==0:
#             return True
#         return False
import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses
numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, prerequisites))