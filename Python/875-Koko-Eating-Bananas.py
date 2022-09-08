class Solution:
    def minSpeed(self, piles: List[int], h: int)-> int:

        # since the h will be at lease len(piles)
        # the max speed we can use is the max of the piles
        # which means we can finish each pile in an hour total of len(piles) hours
        # our approach is to find the min hours from 0 to len(piles) hours
        # for each mid point, we calculate the hours it takes 
        # compare total hours against h
        # if total hours is less than or equal to, meaning the speed is too fast
        
        left, right = 0, max(piles)
        k = 0

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0
            for p in piles:
                total_hours += (p - 1) // mid + 1
            
            if total_hours <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        return k