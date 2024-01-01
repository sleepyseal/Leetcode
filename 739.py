class Solution(object):
    def dailyTemperatures(self, temperatures):
        l=len(temperatures)
        ans=[0]*l
        stack=[]
        for i, t in enumerate(temperatures):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l=len(temperatures)
        ans=[0]*l 
        stack=[]
        index=0
        for i in temperatures:
            if len(stack)==0 or temperatures[stack[-1]]>=i:
                stack.append(index)
                index+=1
            elif temperatures[stack[-1]]<i:
                while len(stack)>0 and temperatures[stack[-1]]<i:
                    ele=stack.pop()
                    ans[ele]=index-ele 
                stack.append(index)
                index+=1
        return ans
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))