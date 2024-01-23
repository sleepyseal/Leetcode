class Solution:
    def restoreIpAddresses(self, s):
        def is_valid(s):
            if int(s)<256 and int(s)>-1:
                if len(s)>1 and s[0]=='0':
                    return False
                return True
            else:
                return False
        def backtracking(s, start_index, path, ans):
            if len(path)==4 and start_index==len(s):
                ans.append(path.copy())
                return
            for i in range(start_index, len(s)):
                if is_valid(s[start_index:i+1]):
                    path.append(s[start_index:i+1])
                    backtracking(s, i+1, path, ans)
                    path.pop()
            return
        ans, path=[], []
        backtracking(s, 0, path, ans)
        res=[]
        for ip in ans:
            cur_ip=''
            for addr in ip:
                cur_ip+=addr+'.'
            res.append(cur_ip[:-1])
        return res
s = "25525511135"
print(Solution().restoreIpAddresses(s))