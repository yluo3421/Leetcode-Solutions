class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        As stated in the problem description, in order to calculate the number of ones in the overlapping zone, we should first shift one of the images. Once the image is shifted, it is intuitive to count the numbers.
        
        Therefore, a simple idea is that one could come up all possible overlapping zones, by shifting the image matrix, and then simply count within each overlapping zone.
        
        Based on the above intuition, we could implement the solution step by step. First we define the function shift_and_count(x_shift, y_shift, M, R) where we shift the matrix M with reference to the matrix R with the shifting coordinate (x_shift, y_shift) and then we count the overlapping ones in the overlapping zone.

The algorithm is organized as a loop over all possible combinations of shifting coordinates (x_shift, y_shift).

More specifically, the ranges of x_shift and y_shift are both [0, N-1] where NN is the width of the matrix.

At each iteration, we invoke the function shift_and_count() twice to shift and count the overlapping zone, first with the matrix B as the reference and vice versa.
        """
        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count, right_shift_count = 0, 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_count += 1
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_count += 1

            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions 
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps