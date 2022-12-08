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
        
        Because largest > rest, we know that x is at most largest - rest. i.e. the modulus will cause rest to be subtracted at least once.

If rest is at least half the size of largest, then this will clearly chop largest in half.

If instead rest is less than half the size of largest, then largest % rest must be less than half of largest.

Removing 1/4 each time is logarithmic.

One edge case we need to be cautious of is where rest is 1. When we take numbers modulo 1, they always become 0. The only case this can occur is where n = 2n=2. In fact though, we know that this case is always doable, because largest is simply decremented by 1 repeatedly until it reaches 1 itself.
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