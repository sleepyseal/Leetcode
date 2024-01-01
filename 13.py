class Solution:
    def romanToInt(self, s):
        d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40,'XC':90, 'CD':400, 'CM':900,}
        ans=0
        l=len(s)
        i=0
        while i<l:
            if s[i]=='I' or s[i]=='X' or s[i]=='C':
                if i<l-1 and s[i:i+2] in d.keys():
                    ans+=d[s[i:i+2]]
                    i+=2
                else:
                    ans+=d[s[i]]
                    i+=1
            else:
                ans+=d[s[i]]
                i+=1
        return ans
s="LVIII"
print(Solution().romanToInt(s))