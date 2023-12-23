class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i=='(':
                stack.append(')')
            if i=='[':
                stack.append(']')
            if i=='{':
                stack.append('}')
            if i==')' or i==']' or i=='}':
                if len(stack)==0:
                    return False
                ele=stack.pop()
                if ele!=i:
                    return False
        if len(stack)>0:
            return False
        return True
