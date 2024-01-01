class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans=[]
        ans.append(intervals[0])
        for i in intervals[1:]:
            if i[0]>ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1]=max(i[1], ans[-1][1])
        return ans
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))