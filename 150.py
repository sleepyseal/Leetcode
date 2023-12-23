class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i !='+' and i !='-' and i !='*' and i !='/' :
                stack.append(i)
            else:
                num2=int(stack.pop())
                num1=int(stack.pop())
                if i=='+':
                    res=num1+num2
                elif i=='-':
                    res=num1-num2
                elif i=='*':
                    res=num1*num2 
                elif i=='/':
                    res=int(float(num1)/float(num2))
                stack.append(res)
        return int(stack[0])

token=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens=token))