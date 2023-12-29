class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        points.sort(key= lambda x: x[0])
        for i in range(1,len(points),1):
            if points[i][0]>points[i-1][1]:
                res+=1
            else:
                points[i][1]=min(points[i][1], points[i-1][1])
        return res+1

points = [[10,16],[2,8],[1,6],[7,12]]
print(Solution().findMinArrowShots(points))
