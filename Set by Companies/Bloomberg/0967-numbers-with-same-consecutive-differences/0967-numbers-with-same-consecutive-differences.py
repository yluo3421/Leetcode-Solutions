class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
        The exit of this dfs is that n == 0, that we have no digits to 
        fill in.
        Based on the last digit of the current number
        Lets call is tail_digit
        We can add difference of k to it, or minus from it
        If the next_digit is valid digit (0-9)
        We dfs to the next level.
        """
        if n == 1:
            return [i for i in range(10)]
        ans = []
        def dfs(n, num):
            if n == 0:
                return ans.append(num)
            tail_digit = num % 10
            next_digits = set([tail_digit + k, tail_digit - k])
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    dfs(n - 1, new_num)
        
        for num in range(1, 10):
            dfs(n - 1, num)
        return list(ans)