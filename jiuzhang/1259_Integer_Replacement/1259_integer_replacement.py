class Solution:
    """
    @param n: a positive integer 
    @return: the minimum number of replacements
    """
    def integer_replacement(self, n: int) -> int:
        # Write your code here
        
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integer_replacement(n // 2)
        return 2 + min(self.integer_replacement(n // 2), self.integer_replacement(n // 2 + 1))

        # Write your code here
        # method 2
        ans = 0
        while n != 1:
            if n % 2 == 0:
                ans += 1
                n //= 2
            elif n % 4 == 1:
                ans += 2
                n //= 2
            else:
                if n == 3:
                    ans += 2
                    n = 1
                else:
                    ans += 2
                    n = n // 2 + 1
        return ans