class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # thoughts
        # pick 2n person to A t
        # now we have pick n to B not the lowest
        # calculate all expenses from switing A to B
        # sort and find first n
        """
                            10                  20
                   30        200          30             200
              400     50   400   50    400    50     400     50
            30 20  30  20 30 20 30 20  30 20  30 20 30 20  30 20
        """
        all_to_a_cost = 0
        switch_a_b_cost = []
        for cost in costs:
            all_to_a_cost += cost[0]
            switch_a_b_cost.append(cost[1] - cost[0])
        switch_a_b_cost.sort()
        ans = all_to_a_cost
        for i in range(int(len(costs) / 2)):
            ans += switch_a_b_cost[i]
        return ans
            
        
    