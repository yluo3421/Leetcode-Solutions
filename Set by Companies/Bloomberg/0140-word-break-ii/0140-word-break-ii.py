class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # dfs
        # after choosing one word, the rest of the s can choose come different
        # answer
        
        """
        catsanddog
        
        cat     cats
        sand    and
        dog     dog
        """
        # backtracking
        # the function checks if from i to j is in words
        # if yes, append this word to path, and check from j position
        # if it reaches end of s, append the joined path to ans
        # if none of the word works, pop the last word from path
        
        def helper(i, path):
            if i == len(s):
                ans.append(" ".join(path))
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    path.append(s[i:j])
                    helper(j, path)
                    path.pop()
        ans = []
        
        path = []
        helper(0, path)
        return ans