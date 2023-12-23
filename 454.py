class Solution(object):
    def hashmap(self, nums1, nums2):
        h={}
        n=len(nums1)
        for i in range(n):
            for j in range(n):
                val=nums1[i]+nums2[j]
                if val in h:
                    h[val]+=1
                else:
                    h[val]=1
        return h 
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans=0
        n=len(nums1)
        h1=self.hashmap(nums1, nums2)
        for i in range(n):
            for j in range(n):
                val=nums3[i]+nums4[j]
                if -val in h1.keys():
                    ans+=h1[-val]
        print(ans)
        return ans
nums1 = [-1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]
Solution().fourSumCount(nums1, nums2, nums3, nums4)