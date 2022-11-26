from typing import (
    List,
)

class Solution:
    """
    @param n: an integer
    @return: 1 - n in lexicographical order
    """
    def lexical_order(self, n: int) -> List[int]:
        # write your code here
        """
        109 < 11 < 110
        DFS and Iteration
        
        """
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans


        """
        Time O(N) | Space O(N)  
        """
        def dfs(temp, n, sol):
            if (temp > n):
                return
            sol.append(temp)
            dfs(temp * 10, n, sol)
            if (temp % 10 != 9):
                dfs(temp + 1, n, sol)
        ans = []
        dfs(1, n, ans)
        return ans
        """
        Time O(Nlog(N)) | Space O(N) 
        """
        s = []
        for i in range(1, n + 1):
            s.append(str(i))
            
        s.sort()
        ans = []
        
        for i in range(n):
            ans.append(int(s[i]))