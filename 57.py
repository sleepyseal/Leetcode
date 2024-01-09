class Solution:
    # def insert(self, intervals, newInterval):
    #     intervals.append(newInterval)
    #     intervals.sort()
    #     ans=[intervals[0]]
    #     for i in intervals[1:]:
    #         if i[0]>ans[-1][1]:
    #             ans.append(i)
    #         else:
    #             ans[-1][1]=max(ans[-1][1], i[1])
    #     return ans
    def binary_search(self, intervals, newInterval):
        l=len(intervals)
        left, right=0, l-1
        target=newInterval[0]
        while left<=right:
            mid=(left+right)//2
            if intervals[mid][0]==target:
                return mid
            elif intervals[mid][0]<target:
                left=mid+1
            else:
                right=mid-1
        return mid+1
    
    def insert(self, intervals, newInterval):
        ans=[]
        if len(intervals)==0:
            return [newInterval]
        if len(newInterval)==0:
            return intervals
        insect=-1
        def is_intersect(l1, l2):
            if l1[1]< l2[0] or l1[0]>l2[1]:
                return False
            return True
        
        for i in intervals:
            if is_intersect(i, newInterval):
                left=min(i[0], newInterval[0])
                right=max(i[1], newInterval[1])
                newInterval=[left, right]
                insect=0
            else:
                if insect==0:
                    ans.append(newInterval)
                    insect=1
                ans.append(i)
        if insect!=1:
            if len(ans)==0:
                return [newInterval]
            index=0
            for i in intervals:
                if i[0]<newInterval[0]:
                    index+=1
                else:
                    break
            ans.insert(index, newInterval)

        return ans        
intervals = [[3,5],[12,15]]
newInterval = [6,6]
print(Solution().insert(intervals, newInterval))
        
