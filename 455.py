class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        len_g=len(g)
        len_s=len(s)
        i, j=0,0
        ans=0
        for i in range(len_g):
            while j<len_s:
                if g[i]>s[j]:
                    j+=1
                else:
                    break
                # else:
                #     break
            if j>=len_s:
                break
            if g[i]<=s[j]:
                ans+=1
                i+=1
                j+=1
            else:
                i=i+1
        return ans
g = [10,9,8,7]
s = [5,6,7,8]
print(Solution().findContentChildren(g,s))