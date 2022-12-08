class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        Time O(n + logk*logn)
        O(n) to create heap, at each step, we remove at least
        1/4 of the total sum. The original total sum is 2k
        because k is the largest element, we know that if the algorithm
        continues, the rest cant add up to more than k.
        So we need to take O(logk) steps to reduce the array
        down. Each of theses steps is the cost of a heap add
        and remove, i.e. O(logn)
        Space O(n)
        
        This solves the problem, although it might not be at all obvious why. The key ideas are:

That largest is always at least half of total_sum.
That largest is always replaced with a value at most half of itself.
        
        We define rest = total_sum - largest. it is the sum of
        the array, excluding the largest
        To prove the first point, we know that largest is always
        bigger than rest. Because if it wasn't, 
        """
        
        # Handle the n = 1 case.
        if len(target) == 1:
            return target == [1]

        total_sum = sum(target)

        target = [-num for num in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            rest = total_sum - largest

            # This will only occur if n = 2.
            if rest == 1:
                return True

            x = largest % rest

            # If x is now 0 (invalid) or didn't
            # change, then we know this is impossible.
            if x == 0 or x == largest:
                return False
            heapq.heapreplace(target, -x)
            total_sum = total_sum - largest + x

        return True