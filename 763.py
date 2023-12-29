class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dic={}
        index=0
        for i in s:
            if i in dic.keys():
                dic[i]=[dic[i][0],index]
            else:
                dic[i]=[index, index]
            index+=1
        interval=[]
        for j in dic.values():
            interval.append(j)
        ans=[]
        for i in range(1, len(interval),1):
            if interval[i][0]<interval[i-1][1]:
                interval[i][1]=max(interval[i][1], interval[i-1][1])
            else:
                ans.append(interval[i-1][1]+1)
        ans.append(len(s))
        res=[]
        for i in range(len(ans)):
            if i==0:
                res.append(ans[i])
            else:
                res.append(ans[i]-ans[i-1])
        return res
s="caedbdedda"
print(Solution().partitionLabels(s))