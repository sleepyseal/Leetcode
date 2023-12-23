class Solution(object):
    def queue(self, q, k):
        if k<q[-1]:
            return q
        for i in range(len(q)-1, -1,-1):
            if q[i]<k:
                q.pop()
            elif q[i]>=k:
                q.append(k)
                break
        if len(q)==0:
            q.append(k)
        return q 
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        q=[-1000000]
        for i in range(k):
            self.queue(q, nums[i])
        ans.append(q[0])
        remove=0
        for i in nums[k:]:
            self.queue(q, i)
            remove_ele=nums[remove]
            if remove_ele==q[0]:
                q.pop(0)
            ans.append(q[0])
            remove=remove+1
        return ans
nums=[1, -1]
k=1
print(Solution().maxSlidingWindow(nums, k))