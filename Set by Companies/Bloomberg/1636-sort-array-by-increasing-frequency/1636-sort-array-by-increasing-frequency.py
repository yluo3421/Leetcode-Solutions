class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # thoughts:
        # go through the array and store its value and freq using a dict
        # push them as tuple and sort by freq
        # push them as result
        # nums = [1,1,2,2,2,3]


        freq_dict = Counter(nums)
        # freq_dict = {1:2,2:3,3:1}

        freq = []
        for key, value in freq_dict.items():
            freq.append((key, value))
        # freq = [(1,2), (2,3), (3,1)]

        # use two sorts to sort them
        # the first sort finds its order by value
        # the second sort finds its order by times
        freq.sort(key = lambda x: x[0], reverse = True)
        # freq = [(3,1), (2,3), (1,2)]
        freq.sort(key = lambda x: x[1])
        # freq = [(3,1), (1,2), (2,3)]

        ans = []
        for item in freq:
            key, times = item
            ans.extend([key] * times)
        return ans
        """
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
        """