class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        Split a factory with limit lim into lim factories with limit 1.

dp[i][j] = the best cost to solve 0 to i robots with 0 to j factories (splited factories). So

dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + cost(i, j)).
Notice that all dp[ i][j] only use info from dp[ i][j-1]. So we can save some memory space by doing this DP is a good order.

Bottom-up version DP
        """
        
        robot.sort()
        factory.sort()
        dp = [0] + [float('inf')] * len(robot)
        for j, (f, l) in enumerate(factory):
            for _ in range(l):
                for i in range(len(robot), 0, -1):
                    dp[i] = min(dp[i], dp[i-1] + abs(robot[i-1]-f))
        return dp[-1]