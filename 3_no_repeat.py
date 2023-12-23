class Solution(object):
    def check_length(self, length, s):
        for i in range(len(s)-length+1):
            set_s=set(s[i:i+length])
            if len(set_s)==length:
                return True
        return False
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length_max=len(set(s))
        length_min=1
        if len(s)==length_max:
            return length_max
        i=length_max
        while True:
            if self.check_length(i, s):
                return i
            else:
                i=i-1
            if i== length_min:
                break
        return i
s=Solution()
string= "abcabcbb"      
print(s.lengthOfLongestSubstring(string))