class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Perform Brute Force Recursion
        1. At any state of recursion, we would be having 
        a piece of rod (or wood), from index l to index r.
        2. Try all the possible cuts on this segment, which 
        splits it into further 2 segments and recurse for 
        the minimum cost in which those 2 segments can be made.

        3. The minimum cost among all those possible cuts + the 
        cost of making our current cut, would be our best cost 
        for cutting the wood in this segment, i.e. from l to r.
        
        4. Memoize the minimum cost for the current l and r value in a memo.
            If the answer for l to r was already present in 
            our memo, then directly retrun the value stored 
            in the memo corresponding to this l and r instead of 
            performing from step 1.
        """
        cuts.sort()
        A = [0] + cuts + [n] # add 2 fake cuts as the boundary of the first cut
        
        def dfs(i, j, A, dp):
            if i > j:
                return 0
			# check the memoization cache
            if dp[i][j] != -1:
                return dp[i][j]
            
            mini = float("inf")
            for k in range(i, j+1):
                cost = A[j+1]-A[i-1] + dfs(i, k-1, A, dp) + dfs(k+1, j, A, dp)
                mini = min(cost, mini)
            
			# set the computed value so we don't have to recompute
            dp[i][j] = mini
            return mini
                
		# build our len(cuts)*len(cuts) 2D array cache
        dp = [[-1 for j in range(len(cuts)+1)] for i in range(len(cuts)+1)]
        
        res = dfs(1, len(cuts), A, dp)
        return res
        
    
    