class Solution:
    def strStr(self, haystack, needle):
        fast, slow=0, 0
        for fast in range(len(haystack)-len(needle)+1):
            if haystack[fast]==needle[slow]:
                match = True
                record=fast
                while slow< len(needle) and fast<len(haystack):
                    if haystack[fast]==needle[slow]:
                        fast+=1
                        slow+=1
                    else:
                        match =False
                        slow=0
                        break 
                if match:
                    return record
            else:
                fast=fast+1
                slow=0
        return -1
h="mississippi"
n='pi'
print(Solution().strStr(h, n))    