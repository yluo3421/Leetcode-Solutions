

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # use heap to record
        # The heap data structure gives us O(1)O(1) access to the minimum 
        # element and log(N)log(N) removal of the minimum element and addition 
        # of a new one. We just need to perform this operation K times to get 
        # our Kth smallest number. In this case, we can safely discard the rows 
        # in the lower part of the matrix i.e. in this case starting from 
        # the 6th row to the end of the matrix because the columns are sorted 
        # as well. So, we need the min(N, K)min(N,K) rows essentially to 
        # find out the answer.
        n = len(matrix)
        priorityqueue = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(priorityqueue)

        
        for i in range(k - 1):
            num, row, col = heapq.heappop(priorityqueue)
            if col != n - 1:
                heapq.heappush(priorityqueue, (matrix[row][col + 1], row, col + 1))
        
        return heapq.heappop(priorityqueue)[0]
        
        