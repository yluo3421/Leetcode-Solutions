class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Initialize sample string "123456789". This string contains all integers that have sequential digits as substrings. Let's implement sliding window algorithm to generate them.

Iterate over all possible string lengths: from the length of low to the length of high.

For each length iterate over all possible start indexes: from 0 to 10 - length.

Construct the number from digits inside the sliding window of current length.

Add this number in the output list nums, if it's greater than low and less than high.

Return nums.
        """
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums