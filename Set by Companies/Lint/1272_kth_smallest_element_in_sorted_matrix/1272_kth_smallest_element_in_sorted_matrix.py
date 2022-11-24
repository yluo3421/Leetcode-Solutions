from typing import (
    List,
)
import heapq
class Solution:
    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """
        [
            [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15]
            ]
        thoughts:
        for each row, we have a start num
        [1,10,12] i in range(7)
        1, x= 0,y = 0
        [5,10,12]
        Time O(nlog(n) + klog(n)) | Space O(n)
        """
        n = len(matrix)
        priorityqueue = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(priorityqueue)

        
        for i in range(k - 1):
            num, x, y = heapq.heappop(priorityqueue)
            if y != n - 1:
                heapq.heappush(priorityqueue, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(priorityqueue)[0]