class Solution:
    def longestCommonPrefix(self, strs):
        min_length=200
        if len(strs)==1:
            return strs[0]
        for i in strs:
            min_length=min(min_length, len(i))
        if min_length==0:
            return ''
        match=True
        index=0
        for index in range(min_length):
            temp=strs[0][index]
            for j in strs[1:]:
                if temp!=j[index]:
                    match=False
                    break
            if match is not True:
                break
        if match==True:
            return strs[0][:index+1]
        return strs[0][:index]
strs = ["abab","aba",""]
print(Solution().longestCommonPrefix(strs))