from typing import (
    List,
)

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    we will sort your return value in output
    Time
    """
    def generate_parenthesis(self, n: int) -> List[str]:
        # write your code here
        result = []
        self.dfs(0, 0, "", n, result)
        return result
    
    def dfs(self, left_count, right_count, nowSeq, n, result):
        if left_count > n or right_count > n:
            return 
        
        if left_count < right_count:
            return
        
        if left_count == n and right_count == n:
            result.append(nowSeq)
        
        self.dfs(left_count + 1, right_count, nowSeq + "(", n, result)

        self.dfs(left_count, right_count + 1, nowSeq + ")", n, result)
