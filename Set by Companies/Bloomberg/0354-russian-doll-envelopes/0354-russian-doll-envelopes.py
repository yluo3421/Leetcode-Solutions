class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        The problem boils down to a two dimensional version 
        of the longest increasing subsequence problem (LIS).

        We must find the longest sequence seq that the elements
        in seq[i+1] are greater than the corresponding elements in
        seq[i]
        
        We answer the question from the intuition by sorting. 
        Let's pretend that we found the best arrangement of 
        envelopes. We know that each envelope must be increasing 
        in w, thus our best arrangement has to be a subsequence 
        of all our envelopes sorted on w.

        After we sort our envelopes, we can simply find the 
        length of the longest increasing subsequence on the 
        second dimension (h). Note that we use a clever trick 
        to solve some edge cases
        
        Consider an input [[1, 3], [1, 4], [1, 5], [2, 3]]. 
        If we simply sort and extract the second dimension we 
        get [3, 4, 5, 3], which implies that we can fit three 
        envelopes (3, 4, 5). The problem is that we can only 
        fit one envelope, since envelopes that are equal in the 
        first dimension can't be put into each other.

        In order fix this, we don't just sort increasing in the 
        first dimension - we also sort decreasing on the second 
        dimension, so two envelopes that are equal in the first 
        dimension can never be in the same increasing subsequence.
        
        Time O(nlogn) | Space O(n)
        """
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([i[1] for i in envelopes])