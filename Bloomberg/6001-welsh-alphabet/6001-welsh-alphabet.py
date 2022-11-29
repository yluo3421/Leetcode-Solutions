class Solution:
    def welsh_sort(self, words):
        # thoughts:
        # given a list of words in welsh
        # sort it in welsh alphabetical order
        # we need to be able to identify each char/double char
        # and find their position
        
        # first give welsh an order with dict
        # then function to check all welsh char
        # then function to check two words
        original = "a b c ch d dd e f ff g ng h i j l ll m n o p ph r rh s t th u w y"
        arr = original.spilt(" ")
        welsh_dict = {}
        for i in range(len(arr)):
            welsh_dict[arr[i]] = i

        def checkChar(word, i):
            if word[i] in "cdfnlprt":
                if i == len(word) - 1:
                    return True
                else:
                    if word[i:i + 2] in original:
                        return False

        def compare(word1, word2):
            n = min(len(word1), len(word2))
            i = 0
            while i < n:
                # first confirm the char
                if checkChar(word1, i):
                    char1 = word1[i]
                else:
                    char1 = word1[i:i + 2]
                if checkChar(word2, i):
                    char2 = word2[i]
                else:
                    char2 = word2[i:i + 2]
                
                # then compare char
                if char1 == char2:
                    i += len(char1)
                elif welsh_dict[char1] < welsh_dict[char2]:
                    return True
                elif welsh_dict[char1] > welsh_dict[char2]:
                    return False

    