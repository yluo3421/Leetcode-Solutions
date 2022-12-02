class Solution:
    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        if not board:
            return False
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ans = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ans = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ans: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ans

# BELOW ANSWERS works too but sometimes time out
class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                wordFound = self.helper(board, word, i, j)
                if wordFound:
                    return True

        return False
        

    def helper(self, board, target, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
            # out of bounds
            return False
        elif board[x][y] == '##':
            # seen this position before
            return False
        elif board[x][y] != target[0]:
            # this position doesn't equal what we want, return False
            return False
        else:
            target = target[1:]
            if not target:
                # word is empty
                return True
            
            # mark board
            saveChar = board[x][y]
            board[x][y] = '##'
            
            down = self.helper(board, target, x + 1, y)
            if down: return down
            left = self.helper(board, target, x, y - 1)
            if left: return left
            right = self.helper(board, target, x, y + 1)
            if right: return right
            up = self.helper(board, target, x - 1, y)
            if up: return up
            # backtrack, unvisiting this position
            board[x][y] = saveChar
            
            return False