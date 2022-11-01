class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # thoughts:
        # go through each station and calculate the result
        # O(n^2)
        
        # to save time, the calc of first station can be used
        # when we start from second station and circle back to first statin
        
        tank_gas_remain = 0
        total_gas_remain = 0
        start_idx = 0
        
        for i in range(len(gas)):
            total_gas_remain += gas[i] - cost[i]
            tank_gas_remain += gas[i] - cost[i]
            if tank_gas_remain < 0:
                start_idx = i + 1
                tank_gas_remain = 0
        if total_gas_remain < 0:
            return -1
        else:
            return start_idx