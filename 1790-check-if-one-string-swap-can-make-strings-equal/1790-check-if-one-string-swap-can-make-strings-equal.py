class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2: #strings are equal no swapping required
            return True
        if sorted(s1)!=sorted(s2): #if alphabets of strings are not equal
            return False
        countof=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:#checking diff aplphabets of both the strings
                countof +=1
        if countof!=2:
                return False
        return True