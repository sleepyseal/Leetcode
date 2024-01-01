class Solution:
    def lengthOfLastWord(self, s):
        l=len(s)
        for i in range(l-1, -1,-1):
            if s[i]!=' ':
                break
        
        fast, slow= i, i
        for i in range(i, -1,-1):
            if s[i]==' ':
                break
            else:
                fast-=1
        return -fast+slow
s ="    fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))