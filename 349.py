class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1={}
        dict2={}
        for i in nums1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in nums2:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
        key1=dict1.keys()
        key2=dict2.keys()
        ans=[]
        for k in key1:
            if k in key2:
                ans.append(int(k))
        return ans
nums1 = [1,2,2,1,1]
nums2 = [2,2,1]
print(Solution().intersection(nums1, nums2))