class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        # dfs
        ans = []
        self.dfs(s, ans, [])
        return ans
    
    def dfs(self, s, ans, path):
        if len(s) == 0:
            ans.append(list(path))
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.isPalindrome(prefix):
                path.append(prefix)
                self.dfs(s[i:], ans, path)
                path.pop()
    
    def isPalindrome(self, s):
        return s == s[::-1]