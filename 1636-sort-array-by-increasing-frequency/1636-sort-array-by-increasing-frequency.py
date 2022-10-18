class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # thoughts:
        # go through the array and store its value and freq using a dict
        # push them as tuple and sort by freq
        # push them as result
        freq = Counter(nums).most_common()
        freq.sort(key = lambda x: x[0], reverse=True)
        freq.sort(key = lambda x: x[1])
        
        ans = []
        for item in freq:
            key, times = item
            ans.extend([key]*times)
            
        return ans
        