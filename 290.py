class Solution:
    def wordPattern(self,  pattern, s):
        ele_s=s.split(' ')
        l, l_s=len(pattern), len(ele_s)
        if l!=l_s:
            return False
        dic_s={}
        for i in range(l):
            if ele_s[i] in dic_s.keys():
                if dic_s[ele_s[i]]!=pattern[i]:
                    return False
            else:
                dic_s[ele_s[i]]=pattern[i]
        set_s=set()
        set_p=set()
        for k, v in dic_s.items():
            set_s.add(k)
            set_p.add(v)
        if len(set_p)!=len(set_s):
            return False
        return True