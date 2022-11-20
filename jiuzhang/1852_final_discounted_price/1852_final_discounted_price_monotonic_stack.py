from typing import (
    List,
)

class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def final_discounted_price(self, prices: List[int]) -> List[int]:
        # write your code here
        # use monotonic stack
        # 因为每个元素入栈出栈各一次，所以是2O(n)
        stack = []
        results = list(prices)
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                results [stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop(-1)
            stack.append(i)
        return results