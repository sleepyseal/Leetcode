class Solution:
    def is_prime(self, n, prime_list):
        for i in prime_list:
            if n%i==0:
                return False
        return True
    
    def prime_num(self, n):
        res=[2]
        next_num=res[-1]+1
        while len(res)<n:
            if self.is_prime(next_num, res):
                res.append(next_num)
            next_num+=1
        return res
    def groupAnagrams(self, strs):
        res=[]
        prime_list=self.prime_num(26)
        dic_s={}
        for s in strs:
            s_value=1
            for e in s:
                s_value*=prime_list[ord(e)-ord('a')]
            if s_value in dic_s.keys():
                dic_s[s_value].append(s)
            else:
                dic_s[s_value]=[s]
        for k, v in dic_s.items():
            res.append(v)
        return res
strs = ["fan","wad"]
print(Solution().groupAnagrams(strs))