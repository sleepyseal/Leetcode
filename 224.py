class Solution:
    def calculate(self, s):
        stack=[]
        def process(aux_stack):
            res=''
            op_num=''
            operate=''
            if aux_stack[0]=='-' or aux_stack[0]=='+':
                aux_stack.insert(0, '0')
            for i in aux_stack:
                if i!='+' and i!='-':
                    op_num+=i
                elif (i=='+' or i=='-') and res=='':
                    if op_num!='':
                        res=int(op_num)
                        operate=i
                        op_num=''
                else:
                    if res!='' and len(op_num)>0:
                        if operate=='+':
                            res+=int(op_num)
                        else:
                            res-=int(op_num)
                        operate=i
                    op_num=''

            if operate=='+':
                res+=int(op_num)
            elif operate=='-':
                res-=int(op_num)
            if res=='':
                return op_num            
            return str(res)
        
        for i in s:
            if i!=')':
                stack.append(i)
            else:
                aux_stack=[]
                while stack[-1]!='(':
                    ele=stack.pop()
                    if ele!=' ':
                        aux_stack.insert(0, ele)
                stack.pop()
                stack.append(process(aux_stack))
        ans=process(stack)
        return int(ans)
s = "1-(     -2)"
print(Solution().calculate(s))
        

                