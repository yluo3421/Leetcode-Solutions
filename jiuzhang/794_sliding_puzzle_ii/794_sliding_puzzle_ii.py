from typing import (
    List,
)

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def min_move_step(self, init_state: List[List[int]], final_state: List[List[int]]) -> int:
        # # write your code here
        """
        How to implement one move
        Use a function and Find 0 and swap with number in four directions

        """
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)

        from collections import deque
        queue = deque([source])
        distance = {source: 0}

        while queue:
            curt = queue.popleft()
            if curt == target:
                return distance[curt]
            for next in self.get_next(curt):
                if next in distance:
                    continue
                    
                queue.append(next)
                distance[next] = distance[curt] + 1
        return -1
    
    def matrix_to_string(self, state):
        str_list = []
        for i in range(3):
            for j in range(3):
                str_list.append(str(state[i][j]))
        return "".join(str_list)

    def get_next(self, state):
        states = []
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1))

        zero_index = state.find("0")
        x, y = zero_index // 3, zero_index % 3

        for i in range(4):
            x_, y_ = x + direction[i][0], y + direction[i][1]
            if 0 <= x_ < 3 and 0 <= y_ < 3:
                next_state = list(state)
                next_state[x * 3 + y] = next_state[x_ * 3 + y_]
                next_state[x_ * 3 + y_] = "0"
                states.append("".join(next_state))
            return states