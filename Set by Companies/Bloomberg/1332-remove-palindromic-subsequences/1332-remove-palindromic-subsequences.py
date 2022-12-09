class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
You need to know the difference between subarray and subsequence.
Subarray need to be consecutive。
Subsequence don't have to be consecutive.


Intuition
If it's empty sting, return 0;
If it's palindrome, return 1;
Otherwise, we need at least 2 operation.


Explanation
We can delete all characters 'a' in the 1st operation,
and then all characters 'b' in the 2nd operation.
So return 2 in this case


Complexity
Time O(N)
Space O(N), also O(1) space checking palindrome is suuggested.        

        The key observation to make is that any sequence of the same letter is a palindrome. For example a, aa, aaa, aaaaaaaa, etc. Because there are only 2 unique letters that can appear in the string, we know we can always solve the problem with at most 2 steps. i.e.

Remove all the a's as a single palindromic subsequence.
Remove all the b's as a single palindromic subsequence.
This leaves us with only 3 possible answers for any given string: 0, 1, or 2. We will need to classify each string we're given into one of these 3 categories. If you haven't yet solved the problem, have another think about how you could do this before you read on.
        
        

        """
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2