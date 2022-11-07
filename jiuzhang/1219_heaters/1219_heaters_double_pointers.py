from typing import (
    List,
)

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    Double pointer at two arrays
    O(nlog(n) + mlog(m)) Time | O(1) Space
    如果给我的已经排好序，双指针可以做到O(N)
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        # sort the array for binary search
        heaters.sort()
        houses.sort()

        house_count = len(houses)
        heaters_count = len(heaters)
        house_idx = 0
        heater_idx = 0
        min_heat_radius = 0

        while (house_idx < house_count) and heater_idx < heaters_count:
            # the heat radius from curr house to curr heater
            curr_radius = abs(houses[house_idx] - heaters[heater_idx])

            # find next heater to curr_house
            # if None, return float("inf")
            # else, calculate heat radius of next heater to curr_house
            if heater_idx < heaters_count - 1:
                next_radius = abs(houses[house_idx] - heaters[heater_idx + 1])
            else:
                next_radius = float("inf")
            
            # if curr heater to curr house has less heat radius
            # then they are the better match we update the min_heat_radius
            if curr_radius < next_radius:
                min_heat_radius = max(min_heat_radius, curr_radius)
                # go to next house
                house_idx += 1
            else:
                # if curr_house is closer to next_heater we cant assume
                # the next heater is the best match, the one after next heater
                # might be a better match. 
                # set next heater as curr heater in next while loop to check
                heater_idx += 1
    
        return min_heat_radius