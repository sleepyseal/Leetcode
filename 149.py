class Solution:
    def maxPoints(self, points):
        ans=0
        if len(points)<=2:
            return len(points)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, x2, y1, y2=points[i][0],points[j][0],points[i][1],points[j][1]
                count=2
                for k in range(j+1, len(points)):
                    x, y=points[k][0], points[k][1]
                    if (y-y1)*(x1-x2)==(y1-y2)*(x-x1):
                        count+=1
                ans=max(ans, count)
        return ans