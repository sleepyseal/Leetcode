class Solution:
    def generateParenthesis(self, n):
        def generate_binary(n):
            ans=[]
            for i in range(n):
                ans.append('(')
            for i in range(n):
                ans.append(')')
            return ans
        def is_valid(array):
            flag=0
            for i in array:
                if i=='(':
                    flag+=1
                else:
                    flag-=1
                if flag<0:
                    return False
            return True
        def backtracking(array, used, path, ans):
            if len(path)==len(array) and is_valid(path):
                ans.append(path.copy())
                return
            ele=float('inf')
            for i in range(0, len(array)):
                if array[i]!=ele and used[i] is False:
                    path.append(array[i])
                    used[i]=True
                    backtracking(array, used, path, ans)
                    ele=path.pop()
                    used[i]=False
        def post_pro(ans):
            res=[]
            for i in ans:
                res.append(''.join(i))
            return res
        ans, path, used= [], [],[False]*n*2
        targe_array=generate_binary(n)
        backtracking(targe_array, used, path, ans)
        ans=post_pro(ans)
        return ans
n=3
print(Solution().generateParenthesis(n))