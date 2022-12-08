class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Say the given array is:

        [7, 1, 5, 3, 6, 4].

        If we plot the numbers of the given array on a graph, we get:
        
        The key point is we need to consider every peak 
        immediately following a valley to maximize the profit. 
        In case we skip one of the peaks (trying to obtain more 
        profit), we will end up losing the profit over one of 
        the transactions leading to an overall lesser profit.
        
        Time O(n) | Space O(1)



  
          
        """
        i = 0
        n = len(prices)
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit
    
        """
        but we can directly keep on adding the difference 
          between the consecutive numbers of the array if the
          second number is larger than the first one, and at 
          the total sum we obtain will be the maximum profit.
        """
        max_profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit