from typing import (
    List,
)

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        # method 1
        # if two run is allowed, this method takes counter of all nums
        #
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1
            
        for num in nums:
            if counter[num] == 1:
                return num
            if num == number:
                break

        return -1