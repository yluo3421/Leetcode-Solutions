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

"""
Algo 2: Suffix Array { this could be complex }
Above algorithm surely cut many branches that we should not 
explore but algorithm lags in finding the sub-string efficiently.
We can use suffix array. Suffix array can be build in O(n^2) 
or O(n*log(n) * log(n) ) or O(nLog(n) Or even O(n) time.
0 1 2
example [ a, b, ,c ] -> Suffixes array [ abc, bc, c ]
ALSO FIND THE last consonant index {this will help us to find 
the first and last sub-string }

After building a suffix array,
   Now going through suffix array order see if the suffix starts 
   with a vowel and the position is less than that of the last consonant 
   otherwise continue going through the loop. For the first suffix that
    satisfies the above criteria run a loop and find the first consonant. 
    That will be the first string.

   For the second string do the same just iterate through the suffix 
   array from the last and once you hit a vowel, start building the 
   sub-string from that index to last consonant index

    Time complexity: O(n)
    Space: O(n)
"""