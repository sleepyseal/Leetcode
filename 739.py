class Solution(object):
    def dailyTemperatures(self, temperatures):
        l=len(temperatures)
        stack=[]
        ans=[0]*l
        for i in range(l):

            while len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                ele=stack.pop()
                ans[ele]=i-ele
            stack.append(i)
        return ans
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))