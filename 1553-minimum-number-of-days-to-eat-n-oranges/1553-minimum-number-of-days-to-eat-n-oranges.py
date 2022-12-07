from functools import lru_cache
class Solution:
    def minDays(self, n: int) -> int:
        """
        From the actions we can take,
        I think for a certain number, k, of orange
        there is three ways to reach that amount of orange
        
        minDays(i) = min(1+minDays(i-1), 1+minDay(i//2), 1 + minDay(i//3)),                 minDay(i-1) is too slow as only eat 1 orange per day. 
        we need to be greedy to fininsh the orange in minimum days
        , so we only choose i//2 or i//3 path.
        now we have: 
        minDays(i) = min(1+ i%2 + minDay(i//2), 1 + i%2 + minDay(i//3))

        path /2: 1 day to eat half of the orange, 
        and the left i//2 oranges need minDay(i//2) days to finish, 
        plus in order to be able to get to path /2, 
        we need i%2 days to reach that path
        path /3: 1 day to eat 2*(i//3) of the oranges, 
        and the left i//3 oranges need minDay(i//2) days to finish, 
        plus in order to be able to get to path /3, 
        we need i%3 days to reach that path
        """
        @lru_cache()
        def minDays(n: int) -> int:
            if n==1: return 1
            if n==2: return 2
            if n==3: return 2
            return min(1 + n%2 + minDays(n//2), 1+n%3 + minDays(n//3))
        return minDays(n)
        
        @lru_cache
        def dfs(n):
            if n <= 1:
                return n
            
            ans1 = ans2 = ans3 = float("inf")
            if n % 3 == 0:
                ans3 = dfs(n // 3)
            if n % 2 == 0:
                ans2 = dfs(n // 2)
            if n % 2 or n % 3:
                ans1 = dfs(n - 1)
            return min(ans1, ans2, ans3) + 1
        
        return dfs(n)
    
        @lru_cache()
        def minDays(n: int) -> int:
            if n==1: return 1
            if n==2: return 2
            if n==3: return 2
            return min(1 + n%2 + minDays(n//2), 1+n%3 + minDays(n//3))
