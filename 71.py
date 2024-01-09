class Solution:
    def simplifyPath(self, path):
        stack=[]
        if path[-1]!='/':
            path+='/'
        l=len(path)
        i=0
        content=''
        while i<l:
            if path[i]=='/':
                if len(content)>0:
                    if content=='..':
                        if len(stack)>0:
                            stack.pop()
                        content=''
                    elif content=='.':
                        content=''
                    else:
                        stack.append(content)
                    content=''
            else:
                content+=path[i]
            i+=1
        res='/'
        if len(stack)==0:
            return res
        for i in stack:
            res+=i+'/'
        return res[:-1]
path = '/a//b////c/d//././/..'
print(Solution().simplifyPath(path))
        