from typing import (
    List,
)

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    DIRECTIONS = [(1,0), (-1,0), (0, 1), (0, -1)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Boundary Condition
        if word == []:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        # Visited Matrix
        visited = [[False for j in range(n)] for i in range(m)]
        # DFS
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False
    
    def dfs(self, board, word, visited, row, col):
        if word == '':
            return True
        m, n = len(board), len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        if board[row][col] == word[0] and not visited[row][col]:
            visited[row][col] = True
            # row - 1, col
            if (
                self.dfs(board, word[1:], visited, row - 1, col) 
                or self.dfs(board, word[1:], visited, row, col - 1) 
                or self.dfs(board, word[1:], visited, row + 1, col) 
                or self.dfs(board, word[1:], visited, row, col + 1)
                ):
                return True
            else:
                visited[row][col] = False
        return False