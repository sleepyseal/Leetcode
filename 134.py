class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l=len(gas)
        v=[0]*l
        for i in range(l):
            v[i]=gas[i]-cost[i]
        if sum(v)<0:
            return -1
        s=0
        ans=0
        i=0
        while i< l:
            s=s+v[i]
            if s<0:
                s=0
                i=i+1
                ans=i
            else:
                i=i+1
        return ans
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]   
print(Solution().canCompleteCircuit(gas, cost))