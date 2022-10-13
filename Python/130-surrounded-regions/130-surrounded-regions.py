class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # similar to island problem
        # but island problem doesnt require to record surronded region
        # could use array to record surronded region
        # one alternative is to flip unsurronded region to T
        # then flip rest of O, which are surronded region to X
        # then flip T to O
        # reason is that unsurronded region only occur at four sides
        # it's easier to find
        
        # check four neighbors of the cell that are on sides
        # if O flip them to T
        # if out of range, return
        ROW = len(board)
        COL = len(board[0])
        def flip_unsurronded(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or board[row][col] != "O":
                return
            board[row][col] = "T"
            flip_unsurronded(row - 1, col)
            flip_unsurronded(row + 1, col)
            flip_unsurronded(row, col - 1)
            flip_unsurronded(row, col + 1)
        
        # first round to go through the board to 
        # flip unsurronded to T
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == "O" and (row in [0, ROW - 1] or col in [0, COL - 1]):
                    flip_unsurronded(row, col)
                    
        # flip rest of O to X
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        # flip T to O
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == "T":
                    board[row][col] = "O"
        return board
        
                    