class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    Doulbe Pointers
    O(n + m) Time | O(|target| + |source|) 
    loop through the target one time, loop through source twice n + 2m
    two dicts to strore char counts
    """
    def min_window(self, source: str, target: str) -> str:
        # write your code here
        if len(target) == 0 or len(source) == 0:
            return ""
        
        m, n = len(target), len(source)

        target_counter, sub_counter = {}, {}
        for i in range(m):
            target_counter[target[i]] = target_counter.get(target[i], 0) + 1
        
        j = 0
        matched_chars = 0
        start, substring_length = 0, float("inf")
        for i in range(n):
            # j will only move forward when j < n and not enough matched
            while j < n and matched_chars < len(target_counter):
                sub_counter[source[j]] = sub_counter.get(source[j], 0) + 1
                if sub_counter[source[j]] == target_counter.get(source[j], 0):
                    matched_chars += 1
                j += 1
            
            if matched_chars == len(target_counter):
                if substring_length > j - i:
                    substring_length = j - i
                    start = i

            sub_counter[source[i]] -= 1
            if sub_counter[source[i]] == target_counter.get(source[i], 0) - 1:
                matched_chars -= 1
        
        if substring_length == float("inf"):
            return ""
        return source[start : start + substring_length]
