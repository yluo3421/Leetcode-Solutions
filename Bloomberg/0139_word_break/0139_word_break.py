class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s), -1, -1):
            for word in wordDict:
                endIdx = i + len(word)
                if endIdx <= len(s) and s[i:endIdx] == word:
                    dp[i] = dp[endIdx]
                if dp[i]:
                    break
        return dp[0]
        """
        012345678
        leetcodeT
            ^
        TFFFTFFFT
        01234
        abcdT
           ^
        FTTFT   
        """