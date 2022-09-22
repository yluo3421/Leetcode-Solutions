class Solution:
    def findSubstring(str: str) -> int:
        # thoughts 
        # finding substring starting with vowel and ending with consonants
        # is the same for the other way around.
        # if I can find out how many consonants from vowel to end of string
        # I will know how many valid substring starting with this vowel
        # I will use two array to record
        # the number of consonants/vowels from this position to end of string
        # then iterate from beginning of the string to find out which
        # char can be used as start
        # It is not clear if duplicates will be taken
        # but it is easy to remove duplicate by using set of dict

        def ifConsonant(ch):
            return ( 
                ch != "a" and ch != "e" and ch != "i"
                and ch != "o" and ch != "u"
            )
        
        def ifVowel(ch):
            return ( 
                ch == "a" or ch or "e" and ch or "i"
                and ch or "o" and ch or "u"
            )
        
        consonantFromIdx = [0 for _ in range(len(str))]
        vowelFromIdx = [0 for _ in range(len(str))]

        if ifConsonant(str[len(str) - 1]):
            consonantFromIdx[len(str) - 1] = 1
        else:
            vowelFromIdx[len(str) - 1] = 1

        for i in range(len(str) - 2, -1, -1):
            if ifConsonant(str[i]):
                consonantFromIdx[i] = 1 + consonantFromIdx[i + 1]
                vowelFromIdx[i] = vowelFromIdx[i + 1]
            else:
                consonantFromIdx[i] = consonantFromIdx[i + 1]
                vowelFromIdx[i] = 1 + vowelFromIdx[i + 1]
        

        ansStartVowel = 0
        ansStartConsonant = 0
        for i in range(len(str) - 1):
            if ifVowel(str[i]):
                ansStartVowel += consonantFromIdx[i + 1]
            else:
                ansStartConsonant += vowelFromIdx[i + 1]
        return [ansStartConsonant, ansStartVowel]