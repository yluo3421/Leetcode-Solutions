class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # thoughts:
        # push two word into two dict
        # check if they are the same
        
        # new thoughts:
        # list(word) can push word all chars into list
        # sort it, that two anagrams should have the same lists
        # create a table with the sorted list as key, and push all same ones
        # into its value
        
        word_table = {}
        for word in strs:
            word_sorted = "".join(sorted(list(word)))
            if word_sorted not in word_table:
                word_table[word_sorted] = [word]
            else:
                word_table[word_sorted].append(word)
        return list(word_table.values())