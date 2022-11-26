class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def length_of_longest_substring(self, s: str) -> int:
        # write your code here
        # double pointer 模版！
        """
        "abcabcbb"
                ^
                ^
        """
        unique_chars = set([])
        j = 0
        n = len(s)
        longest = 0
        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])
        return longest



        