from typing import (
    List,
)

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    monotonic area
    """
    def maximal_rectangle(self, matrix: List[List[bool]]) -> int:
        # write your code here
        if not matrix:
            return 0
        
        heights = [0] * len(matrix[0])
        max_area = 0

        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num else 0
            max_area = max(max_area, self.largest_rectangle_area(heights))
        return max_area
    
    def largest_rectangle_area(self, heights):
        if not heights:
            return 0
        max_area = 0
        stack = []
        n = len(heights)
        for right_boundary in range(n + 1):
            right_boundary_height = -1 if right_boundary == n else heights[right_boundary]

            while stack and heights[stack[-1]] > right_boundary_height:
                curr_height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                curr_width = right_boundary - left_boundary - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(right_boundary)
        return max_area
