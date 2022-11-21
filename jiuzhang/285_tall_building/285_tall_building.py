from typing import (
    List,
)

class Solution:
    """
    @param arr: the height of all buildings
    @return: how many buildings can he see at the location of each building
    monotonic stack
    """
    def tall_building(self, arr: List[int]) -> List[int]:
        # do monotonic stack from left to right and backward
        # add another 1 as itself so we get answer
        results = [1] * len(arr)
        self.count_buildings(arr, results, range(len(arr)))
        self.count_buildings(arr, results, range(len(arr) - 1, -1, -1))
        return results
    
    def count_buildings(self, arr, results, index_list):
        stack = []
        for i in index_list:
            results[i] += len(stack)
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop(-1)
            stack.append(i)