class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l=len(ratings)
        left=[1]*l
        right=[1]*l
        ans=0
        for i in range(1, l,1):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        for i in range(l-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
        for i in range(l):
            ans+=max(right[i],left[i])
        return ans
ratings = [1,2,87,87,87,2,1]
print(Solution().candy(ratings))
