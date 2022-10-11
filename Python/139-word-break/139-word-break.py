class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use dp to check each word
        # every time checking the char, find if w in wordDict
        # be used to replace.
        # brutal force first
        # I could check every single char, if with that start
        # can the word in wordDict fit.
        # if it fits, increase the pointer by len(word) and check again
        # if it doesnt, return False
        
        """
        def checkFromIdx(i):
            for word in wordDict:
                start = i
                end = i + len(word)
                if word == s[start: end]:
                    
                    if end == len(s):
                        return True
                    return checkFromIdx(end)
            
        return checkFromIdx(0)
        """
        
        # this method only works when no recheck at each char
        # we need to run all words at each char to make sure all checked
        
        # use dp array
        # dp[i] represent if s at index i can be represented as word
        # dp[i + len(word)] = True
        # if dp[-1] == True return True or return False
        # dp 10101
        #    cars
        #    ^
        # we work backward
        # if dp[i] break from iterating through wordDict
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s), -1, -1):
            for word in wordDict:
                endIdx = i + len(word)
                if endIdx <= len(s) and s[i:endIdx] == word:
                    dp[i] = dp[endIdx]
                if dp[i]:
                    break
        print(dp)
        return dp[0]
        
        