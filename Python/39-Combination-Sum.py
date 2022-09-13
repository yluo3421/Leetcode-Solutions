class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # thoughts
        # candidates = [2,3,6,7]
        # if brute force, every time we have 4 choices
        #   2       3       6       7
        #                           7+any number is larger than target
        #                   6+any number is larger than target
        #           3+2, 3+6,3+7, tha latter two doesnt work
        # 2+2, 2+3
        # 2+2+3 2+3+2 gives me duplicates
        # a new binary tree but this time left tree only takes duplicates of
        # current number, while right tree only takes remaining numbers
        #                       start[2]                        start[7]
        #       canditates[2]        [3,6,7]                    
        #->         [2,2]                [2,3]
        #canditates[2]     [3,6,7]         [3]         [6,7]
        #->     [2,2,2]     [2,2,3]        [2,3,3]X      X X
        # canditates[2]     [3]  [6,7]
        #->[2,2,2,2]X       X    X  X
        # results[2,2,3],[7]
        ans = []
        def dfs(i, currentCombination, currentTotal):
            if currentTotal == target:
                ans.append(currentCombination.copy())
                return
            if currentTotal > target or i > len(candidates):
                return

            # left tree that picks the same candidate
            currentCombination.append(candidates[i])
            # continues to check if the total is larget than target
            dfs(i, currentCombination, currentTotal + candidates[i])

            # right tree that picks the remaining candidates
            # but need to drop the canditates[i] first
            currentCombination.pop()
            dfs(i + 1, currentCombination, currentTotal)
        dfs(0, [], 0)
        return ans
