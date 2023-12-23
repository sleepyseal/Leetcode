class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s={}
        dict_t={}
        for i in s:
            if i in dict_s:
                dict_s[i]+=1
            else:
                dict_s[i]=1
        for j in t:
            if j in dict_t:
                dict_t[j]+=1
            else:
                dict_t[j]=1
        if dict_s==dict_t:
            return True
        else:
            return False
s = "anagram"
t = "nagaram"
Solution().isAnagram(s, t)