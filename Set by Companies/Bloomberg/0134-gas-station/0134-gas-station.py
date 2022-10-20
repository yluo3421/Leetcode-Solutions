class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # thoughts:
        # go through each station and calculate the result
        # O(n^2)
        
        # to save time, the calc of first station can be used
        # when we start from second station and circle back to first statin
        
        tank_remain_gas = 0
        total_remain_gas = 0
        start_idx = 0
        
        for i in range(len(gas)):
            total_remain_gas += gas[i] - cost[i]
            tank_remain_gas += gas[i] - cost[i]
            if tank_remain_gas < 0:
                tank_remain_gas = 0
                start_idx = i + 1
        if total_remain_gas < 0:
            return -1
        else:
            return start_idx