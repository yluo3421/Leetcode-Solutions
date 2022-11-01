class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # we need to generate all possible substring
        ans = []
        self.dfs(s, [], ans)
        return ans
    
    def dfs(self, s, path, ans):
        if not s:
            ans.append(path)
            return
        
        for i in range(1, len(s) + 1):
            if self.isParlindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], ans)
    
    def isParlindrome(self, s):
        return s == s[::-1]