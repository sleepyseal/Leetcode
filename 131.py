class Solution:
    def partition(self,s):
        def is_valid(s):
            if len(s)==0:
                return False
            l, r=0, len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtracking(input_str, start_index, path, ans):
            if start_index==len(input_str):
                ans.append(path.copy())
                return
            for i in range(start_index, len(input_str)):
                if is_valid(input_str[start_index:i+1]):
                    path.append(input_str[start_index:i+1])
                    backtracking(input_str, i+1, path, ans)
                    path.pop()
            return
        path, ans=[], []
        backtracking(s, 0, path, ans)
        return ans
s='aab'
print(Solution().partition(s))
