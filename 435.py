class Solution(object):
    # def eraseOverlapIntervals(self, intervals):
    #     """
    #     :type intervals: List[List[int]]
    #     :rtype: int
    #     """
    #     ans=0
    #     intervals.sort(key=lambda x: x[0])
    #     for i in range(1, len(intervals), 1):
    #         if intervals[i][0]>=intervals[i-1][1]:
    #             pass
    #         else:
    #             intervals[i][1]=min(intervals[i-1][1], intervals[i][1])
    #             ans+=1
    #     return ans
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans=0
        intervals.sort(key=lambda x: x[0])
        d=[0]*len(intervals)
        d[0]=0
        right=intervals[0][1]
        index=1
        for i in intervals[1:]:
            if i[0]<right:
                d[index]=d[index-1]+1
                right=min(i[1], right)
            else:
                right=i[1]
                d[index]=d[index-1]
            index+=1
        return d[-1]
intervals = [[1,100],[11,22],[1,11],[2,12]]
print(Solution().eraseOverlapIntervals(intervals))