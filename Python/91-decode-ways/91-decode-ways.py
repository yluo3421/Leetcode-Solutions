class Solution:
    def numDecodings(self, s: str) -> int:
        # thoughts:
        # the char 0 cannot be decoded only used as 2nd digit
        # 1~2 can be decoded to either A B or the 1st digit
        # 3~9 can be decoded to 1st or 2nd digit
        
        # burtal DFS
        # if we treat first char as one option, it can generate a bunch of options
        # if we treat first two char as one option, will generate another set
        # each char can be read as one option
        # the option will be increased if it is 1?, 2?(0~6)
        
        # 12
        # take first char, ans += 1
        # check second char, can be 12, ans += 1
        # take second char ans += 1
        
        # 2026
        # dfs should be done checking each char
        # with 2 digit possible, ans += 1
        # with 0 skip
        dp = {len(s): 1}
        
        # its char so we can use in string to check 0123456
        # cannot use global variable
        # still check backward,
        # if can be taken as 2 digit number, meaning the options at i
        # is 2 times dp[i + 2]
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            ans = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                ans += dfs(i + 2)
            dp[i] = ans
            return ans
        
        return dfs(0)
        