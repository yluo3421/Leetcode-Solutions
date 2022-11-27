class Solution:
    """
    @param s: 
    @return: return a string
    """
    def frequency_sort(self, s: str) -> str:
        # write your code here
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        items = [(key, val) for key, val in count.items()]
        items.sort(key = lambda x:(-x[1], x[0]))
        results = []
        for pair in items:
            for i in range(pair[1]):
                results.append(pair[0])
        return "".join(results)