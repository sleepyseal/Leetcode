class MinStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        self.stack.append(val)
        if len(self.minstack)==0:
            self.minstack.append(val)
        else:
            if val > self.minstack[-1]:
                pass
            else:
                # while len(self.minstack)>0 and self.minstack[-1]>val:
                #     self.minstack.pop()
                self.minstack.append(val)

    def pop(self):
        ele= self.stack.pop()
        if len(self.minstack)>0 and ele== self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        if len(self.minstack)==0:
            return None
        return self.minstack[-1]
    
minStack =MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()