from typing import (
    List,
)

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    Binary search
    O((n + m) * log(m)) Time | O(1) Space
    O(mlogm) to sort heaters, O(n) to find all houses
    find the position house within all heaters binary serach, o(logm)

    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        # sort the array for binary search
        heaters.sort()
        min_heat_radius = 0
        for house in houses:
            radius = self.get_minimum_radius(house, heaters)
            min_heat_radius = max(min_heat_radius, radius)
        return min_heat_radius
    
    # find the closest heater to the house, return the distance
    def get_minimum_radius(self, house, heaters):
        left_heater, right_heater = 0, len(heaters) - 1
        while left_heater + 1 < right_heater:
            mid_heater = (left_heater + right_heater) // 2
            # if house is at right of the mid_heater, discard the left part
            if heaters[mid_heater] <= house:
                left_heater = mid_heater
            else:
                right_heater = mid_heater
        
        left_distance = abs(heaters[left_heater] - house)
        right_distance = abs(heaters[right_heater] - house)
        return min(left_distance, right_distance)