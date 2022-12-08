class RangeModule:
    """
    We make use of the python bisect_left and bisect_right 
    functions. bisect_left returns an insertion index in a 
    sorted array to the left of the search value. bisect_right 
    returns an insertion index in a sorted array to the 
    right of the search value. See the python documentation. 
    To keep track of the start and end values of the ranges 
    being tracked, we use a tracking array of integers. 
    This array consists of a number of sorted pairs of 
    start and end values. So, it always has an even number 
    of elements.

    addRange first gets the leftmost insertion index of 
    the left value and the rightmost insertion index of 
    the right value. Then, we check if either of these 
    indexes are even. If the index is even, it means that 
    it is currently outside the range of start and end 
    indexes being tracked. In this case, we include this 
    index to be updated in the tracking array. We then use 
    python array slicing to overwrite the tracking array 
    with the left and right values placed in the correct 
    index. Complexity is O(n).

    removeRange first gets the leftmost insertion index of 
    the left value and the rightmost insertion index of the 
    right value. Then, we check if either of these indexes 
    are odd. If the index is odd, it means that it is currently 
    inside the range of start and end indexes being tracked. 
    In this case, we include this index to be updated in the 
    tracking array. We then use python array slicing to overwrite 
    the tracking array with the left and right values placed 
    in the correct index. Complexity is O(n).

    queryRange gets the rightmost insertion index of the left 
    value and the leftmost insertion index of the right value. 
    If both these indexes are equal and these indexes are odd, 
    it means the range queried is inside the range of values 
    being tracked. In this case, we return True. Else, we return 
    False. Complexity is O(log n).
    """

    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
			
        self.track[start:end] = subtrack

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
			
        self.track[start:end] = subtrack
		
    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
		
        return start == end and start % 2 == 1
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)