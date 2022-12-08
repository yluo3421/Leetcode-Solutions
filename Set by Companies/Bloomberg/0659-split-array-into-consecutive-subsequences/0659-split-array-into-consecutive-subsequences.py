class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        This can be better understood with an example. Let's consider an array nums = {1, 2, 3, 5, 6, 8, 9, 10}.

        At 0th index: {1} [new subsequence formed]
        At 1st index: {1, 2} [add to the existing subsequence]
        At 2nd index: {1, 2, 3} [add to the existing subsequence]
        At 3rd index: {1, 2, 3}, {5} [new subsequence formed]
        At 4th index: {1, 2, 3}, {5, 6} [add to the existing subsequence]
        At 5th index: {1, 2, 3}, {5, 6}, {8} [new subsequence formed]

        Initialize two maps - one to store the frequency 
        of each element present in nums array (frequency), 
        the other to store the frequency of subsequences 
        ending with the key (subsequences).

        Iterate over the nums array to update the frequency map.

        Iterate over the nums array.

        If the frequency of the current element num is 0, 
        it means the num is already considered to be a part 
        of a valid subsequence. Continue.

        Next, check if it is possible to add num to one 
        of the existing subsequences. For this, check if 
        there is an entry with key as num - 1 in the subsequences 
        map. If there exists such an entry, it means we can add 
        num to an existing subsequence. Make the necessary changes 
        in subsequences map to keep it consistent.

        If no such subsequence exists, we need to create a 
        new subsequence with num as the first element. For this, 
        we need to check if num + 1 and num + 2 exist or not. 
        If they don't, no valid subsequence is possible with num 
        as the starting element. Return false. Otherwise, make 
        the necessary changes in subsequences map to keep it consistent.

        After the traversal is done, return true.
        """
        subsequences = {}
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            subsequences[num] = 0
        for num in nums:
            # num already part of a valid subsequence.
            if frequency[num] == 0:
                continue
            
            # If a valid subsequence exists with last element = num - 1.
            if num - 1 in subsequences and subsequences[num - 1] > 0:
                subsequences[num - 1] -= 1
                subsequences[num] += 1
            # if we wnat to start a new subsequence,
            # check if num + 1 and num + 2 exists
            elif (
                num + 1 in frequency
                and num + 2 in frequency
                and frequency[num + 1] > 0 
                and frequency[num + 2] > 0
                
            ):
                subsequences[num + 2] += 1
                frequency[num + 1] -= 1
                frequency[num + 2] -= 1
            else:
                # no valid subsequence is possible with num
                return False
            frequency[num] -= 1
        return True
    