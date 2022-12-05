class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
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