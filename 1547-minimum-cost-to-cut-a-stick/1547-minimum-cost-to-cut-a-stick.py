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
        cuts.extend([0, n])  # add 2 fake cuts as the boundary of the first cut
        cuts.sort()
        @functools.lru_cache(None)
        def f(i, j):
            if i + 1 >= j: return 0
            """
            cuts[j] - cuts[i] # cost of the first cut between ith and jth cut
                + min((f(i, k) + f(k, j) for k in range(i+1, j)), default=0)  # go through all the cuts as the first cut
            """
            return cuts[j] - cuts[i] + min((f(i, k) + f(k, j) for k in range(i+1, j)), default=0)
        return f(0, len(cuts)-1)