class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        thoughts:
        anagram are two strings with not only same chars
        but also same amount of each char
        To check if they are anagram, I can put all chars
        into two dicts of the two words
        If they are the same then its anagram and return 0
        If not, I will calculate the difference and that's amount 
        of chars needs to be changed
        Let's use example 2 to do a dry run
        leetcode = {c:1, d:1, e:3, l:1, o:1, t:1 }
        practice = {a:1, c:2, e:1, i:1, p:1, r:1, t:1}
        It is hard to compare in this way, I want to make sure both dict
        has the same keys.
        Here's my plan, I will find out whoever not in s_dict and add
        them in there with value of 0. Same thing to the t_dict.
        Then I will count the diff
        Time complexity of this method will be O(m + n) with length of 
        two strings, Space O(m + n) if they are totally different words
        Is this what you are looking for?
        """
        char_s, char_t = {}, {}
        for char in s:
            char_s[char] = char_s.get(char, 0) + 1
            char_t[char] = char_t.get(char, 0)
        for char in t:
            char_t[char] = char_t.get(char, 0) + 1
            char_s[char] = char_s.get(char, 0)
        ans = 0
        for char in char_s.keys():
            ans += abs(char_s[char] - char_t[char])
        return int(ans/2)