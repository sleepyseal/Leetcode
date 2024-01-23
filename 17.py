class Solution:
    def letterCombinations(self, digits):
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtracking(digits, phoneMap,digit_index, path, ans):
            if len(path)==len(digits):
                cur_res=''
                for ele in path:
                    cur_res+=ele
                ans.append(cur_res)
                return
            content=phoneMap[digits[digit_index]]
            for i in content:
                path.append(i)
                backtracking(digits, phoneMap, digit_index+1, path, ans)
                path.pop()
            return

        path, ans=[], []
        backtracking(digits, phoneMap, 0, path, ans)
        return ans
digits=''
print(Solution().letterCombinations(digits))