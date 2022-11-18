class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # use two pointer at both string
        # check difference char, and record the pair and count
        # if count > 1: return false
        # if the second time matches, yes
        
        if s1 == s2: #strings are equal no swapping required
            return True
        if sorted(s1) != sorted(s2): #if alphabets of strings are not equal
            return False
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:#checking diff aplphabets of both the strings
                count += 1
        if count != 2:
                return False
        return True

                    

            