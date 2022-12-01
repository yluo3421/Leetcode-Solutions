class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # since we are trying to find the optimal solution
        # we can start with a decision tree
        # with example 1
        #       link1                  d-link1
        # link4    d-link4          link 4      d-link4
        #       link2  d-link2                  link2 d-link2
        # the best path is to have most link on the path
        # and we can see d-link4 subtree is calculated twice
        # this to me is a dp problem
        # thus I want to create a dp array to solve this
        # the idea is to use dp[i][j] to show max links found using first
        # i and first j of nums1 and nums2
        n = len(nums1)
        m = len(nums2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # the first row and first col needs to be initialized as 0
        # because using 0 items from one array will give 0 links
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    # meaning this will be one more link then not using
                    # the extra number in both arrays
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # meaning it will inherit the max number of links of 
                    # not using either num in either array
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[n][m]
    