class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        people.sort(key= lambda x: (x[0], -x[1]), reverse=True)
        for i in people:
            index=i[1]
            ans.insert( index,i)
        return ans
people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
print(Solution().reconstructQueue(people))
[[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
[[3, 0], [6, 0], [7, 0], [5, 2], [3, 4], [6, 2], [5, 3], [2, 7], [9, 0], [1, 9]]
[[3, 0], [6, 0], [7, 0], [5, 2], [3, 4], [5, 3], [6, 2], [2, 7], [9, 0], [1, 9]]