class Solution:
    def countDistinct(self, s: str) -> int:
        """
        Brutal force method is to generate all subsets 
        of the string and add to a set
        
        """
        ans_set = set([i for i in s])
        n = len(s)
        for i in range(n):
            temp = s[i]
            for j in range(i + 1, n):
                temp += s[j]
                ans_set.add(temp)
        return len(ans_set)
        