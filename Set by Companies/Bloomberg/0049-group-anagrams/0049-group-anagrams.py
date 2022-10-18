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
            word_sort_char = "".join(sorted(list(word)))
            if word_sort_char not in word_table:
                word_table[word_sort_char] = [word]
            else:
                word_table[word_sort_char].append(word)
        return list(word_table.values())
        """ 
        # below method works but takes too much time
        # O(N^2)
        def check(word1, word2):
            if len(word1) != len(word2):
                
                return False
            word1_dict, word2_dict = {}, {}
            for i in range(len(word1)):
                word1_dict[word1[i]] = word1_dict.get(word1[i], 1) + 1
                word2_dict[word2[i]] = word2_dict.get(word2[i], 1) + 1
            if word1_dict == word2_dict:
                return True
            else:
                return False
            
        if len(strs) == 1:
            return [strs]
        visited = [False for _ in range(len(strs))]
        ans = []
        for i in range(len(strs)):
            if not visited[i]:
                anagrams = [strs[i]]
                visited[i] = True
                j = i + 1
                while j < len(strs):
                    if visited[j] == False:
                        if check(strs[i], strs[j]):
                            anagrams.append(strs[j])
                            visited[j] = True
                    j += 1
                ans.append(anagrams)
        return ans
        """