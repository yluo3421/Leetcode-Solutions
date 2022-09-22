class Solution:
    def minGame(N, K) -> int:
        """
        input: n is the number to be reachd, k is all-in times
        output: min number of rounds needed
        """
        # thoughts:
        # if N > 1: meaning we need to take more rounds to finish
        # if K > 0: meaning we can gamble K times
        # check if N can be divided by two, if yes
        # N /= 2 count ++ K -- 
        # if not divided by two, N -= 1, count ++
        # if K became 0
        # just add the remaining N to the count as the total $1 bet needed

        count = 0
        while N > 1:
            if K > 0:
                if N % 2 == 0:
                    
                    K -= 1
                    N /= 2
                else:
                    N -= 1
                count += 1  
            else:
                count += N - 1
                N = 0
        return count
