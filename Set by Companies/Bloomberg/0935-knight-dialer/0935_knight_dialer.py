class Solution:
    def knightDialer(self, n: int) -> int:
        """
        Oh I miss this keypad, i still had the cell phone I used in
        my middle school. 
        Ok, so I want to first check out what I can do with knight hop
        If I started 1, I can get 6,8, 2:[7,9], 3:[4,8], 4:[3,9,0]

        I don't want to show them all here but currently I have the
        idea that they are like neighbors when I pressed 1.
        So I can definitely go through 10 start key, and check who else I
        can do. And I just realize that 5 cannot go anywhere.

        Everytime I looked at one key, who else I can go to.
        It's a decision tree that leads to several neighbors
        And this is called recursively until ending.
        While subtrees in the decision tree will be exactly the same
        I can put what we found above as a dict to access faster
        And to avoid making same decision we can use dp to solve this

        n rounds means we need to have n rows in dp of 10 columns
        for neighbor in dict[start]:
            dp[n][neighbor] += dp[n - 1][start] 
        
        The Time O(n*10) 
        
        Wait a second, I think I can save some space here by using 
        only last row information. Cause the current row info is only
        based on prev row. I don't need to maintain the whole n rows


        """
        if n == 1:
            return 10
        neighbors = {
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[2,4],
            0:[4,6]
        }
        curr_row = [1] * 10
        for i in range(n - 1):
            next_row = [0] * 10
            for start in range(10):
                for neighbor in neighbors[start]:
                    next_row[neighbor] += curr_row[start]
            curr_row = next_row
        return sum(curr_row) % (10**9 + 7)