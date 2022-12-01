class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        First we need to find all candies that can be removed
        We can go through each line
        if we see 3 in a row, we will mark them as 0
        Then go through each row do the same thing
        Wait, do we have more than 3 combo? like 4 in a row?
        Ok in the exmample it shows we do have more than 3
        So check for all numbers of combo
        Double pointer to scan the line or row
        I just realized that if there is a cross
        Like example 1 first picture it shows 222 in L shape
        What shall I do then ....
        Cause if I mark the row 3 combo first, I will not be able
        to mark the col 3 combo.
        Do you have any good idea about this? I am a little stuck.
        Oh ok I have an idea
        we can first save them as negative ones, when we are checking
        cols we will use absolute value to avoid skipping marked ones

        Second step is to drop all remaining ones after crashing
        for every column, we are going to traverse backwards
        If we found a positive number, swap it so that positive
        number are at the bottom and zeros will be at top
        """
        ROW = len(board)
        COL = len(board[0])
        drop = False

        for row in range(ROW):
            for col in range(COL - 2):
                num1 = abs(board[row][col])
                num2 = abs(board[row][col + 1])
                num3 = abs(board[row][col + 2])
                if num1 == num2 == num3 != 0:
                    board[row][col] = -num1
                    board[row][col + 1] = -num2
                    board[row][col + 2] = -num3
                    drop = True
        
        for row in range(ROW - 2):
            for col in range(COL):
                num1 = abs(board[row][col])
                num2 = abs(board[row + 1][col])
                num3 = abs(board[row + 2][col])
                if num1 == num2 == num3 != 0:
                    board[row][col] = -num1
                    board[row + 1][col] = -num2
                    board[row + 2][col] = -num3
                    drop = True

        # mark those as 0
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] < 0:
                    board[row][col] = 0

        # step 2: drop all candies
        
        for col in range(COL):
            bot_idx = ROW - 1
            for row in range(ROW - 1, -1, -1):
                if board[row][col] > 0:
                    board[bot_idx][col], board[row][col] = board[row][col], board[bot_idx][col]
                    bot_idx -= 1
                    
        return board if not drop else self.candyCrush(board)