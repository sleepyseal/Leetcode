class Solution:
    def isPalindrome(self, s):
        l=len(s)
        left=0
        right=l-1
        while left<right:
            while ((ord(s[left])>=ord('a') and ord(s[left])<= ord('z')) or (ord(s[left])>=ord('A') and ord(s[left])<= ord('Z')) or (ord(s[left])>=ord('0') and ord(s[left])<= ord('9'))) is False:
                left+=1
                if left>=right:
                    return True
            while ((ord(s[right])>=ord('a') and ord(s[right])<= ord('z')) or (ord(s[right])>=ord('A') and ord(s[right])<= ord('Z')) or (ord(s[right])>=ord('0') and ord(s[right])<= ord('9'))) is False:
                right-=1
                if left>=right:
                    return True            
            if ord(s[left])>=ord('A') and ord(s[left])<= ord('Z'):
                ele_left=chr(ord(s[left])+32)
            else:
                ele_left=s[left]
            
            if ord(s[right])>=ord('A') and ord(s[right])<= ord('Z'):
                ele_right=chr(ord(s[right])+32)
            else:
                ele_right=s[right]
            
            if ele_left==ele_right:
                left+=1
                right-=1
            else:
                return False
        return True
    
s = "0P"
print(Solution().isPalindrome(s))