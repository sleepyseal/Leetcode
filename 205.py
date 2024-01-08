class Solution:
    def isIsomorphic(self, s, t):
        dic_compare={}
        l, l_t=len(s), len(t)
        if l!=l_t:
            return False
        for i in range(l):
            if s[i] in dic_compare.keys():
                if dic_compare[s[i]]!=t[i]:
                    return False
            else:
                dic_compare[s[i]]=t[i]
        k_ele=set()
        v_ele=set()
        for k, v in dic_compare.items():
            v_ele.add(v)
            k_ele.add(k)
        if len(k_ele)!=len(v_ele):
            return False
        return True
