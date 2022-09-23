

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        priorityqueue = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(priorityqueue)

        
        for i in range(k - 1):
            num, row, col = heapq.heappop(priorityqueue)
            if col != n - 1:
                heapq.heappush(priorityqueue, (matrix[row][col + 1], row, col + 1))
        
        return heapq.heappop(priorityqueue)[0]
        
        