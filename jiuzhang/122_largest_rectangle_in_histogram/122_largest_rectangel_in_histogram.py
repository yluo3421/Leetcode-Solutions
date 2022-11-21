from typing import (
    List,
)

class Solution:
    """
    @param heights: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largest_rectangle_area(self, heights: List[int]) -> int:
        # write your code here
        if not heights:
             return 0
            
        max_area = 0
        n = len(heights)
        stack = []

        for right_boundary in range(n + 1):
            # 如果右边界，可以认为右边界一并比站定元素矮， 设定为-1
            # -1 必定小于界内任何数字，因为界内都是非负数
            right_boundary_height = -1 if right_boundary == n else heights[right_boundary]

            # 如果站定高度大于当前高度
            # 则right_boundary_height是栈顶元素右侧离它最近的第一个比它小的高度
            while stack and heights[stack[-1]] > right_boundary_height:
                # pop当前栈顶元素，作为矩形高度
                curr_height = heights[stack.pop()]
                # curr_height被弹出以后，因为是单调递增栈，当前栈顶元素是curr_height
                # 左侧 离它最近的第一个比它小的高度。如果栈为空，左边界下标为-1
                left_boundary = stack[-1] if stack else -1
                # 左右边界之间距离为矩形宽度，注意需要-1
                curr_width = right_boundary - left_boundary - 1
                max_area = max(max_area, curr_width * curr_height)
            # 当前元素必定入栈，注意入栈的是下标
            stack.append(right_boundary)
        return max_area