class Solution:
    def isSubsequence(self, s, t):
        if len(s)>len(t):
            return False
        t_index=0
        for i_s in s:
            if t_index>len(t)-1:
                return False
            if i_s ==t[t_index]:
                t_index+=1
                continue
            else:
                while i_s!=t[t_index]:
                    if t_index>=len(t)-1:
                        return False
                    else:
                        t_index+=1
                t_index+=1
        return True   
s ="bcd"
t ="ubcd"            
print(Solution().isSubsequence(s, t))