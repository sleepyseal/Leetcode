from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        d_s= sorted(d, key=d.get, reverse=True)
        return d_s[:k]

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))