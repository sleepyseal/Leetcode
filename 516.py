class Solution:
    def longestPalindromeSubseq(self, s):
        l=len(s)
        dp=[]
        res=0
        for i in range(l+1):
            dp.append([0]*(l+1))

        dp[0][0]=1

        for i in range(l-1, 0, -1):
            for j in range(i, l+1):
                if s[i-1]==s[j-1]:
                    if j-i<=1:
                        dp[i][j]=j-i+1
                    elif dp[i+1][j-1]>0:
                        dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
                if dp[i][j]>res:
                    res=dp[i][j]
        return res  
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
print(Solution().longestPalindromeSubseq(s))