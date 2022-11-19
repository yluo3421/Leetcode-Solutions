class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # for a three candies combo
        # we have to pay for the most expensive two to get the
        # third one free
        # sort the input and get three at a time
        # if number of candies is less than 3 we have to pay all
        
        sorted_cost = sorted(cost, reverse = True)
        print(sorted_cost)
        count = 1
        total = 0
        n = len(sorted_cost)
        i = 0
        while i < n:
            print(i)
            if count == 1 or count == 2:
                total += sorted_cost[i]
                count += 1
                i += 1
            if count == 3:
                count = 1
                i += 1
        return total