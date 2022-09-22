class Solution:
    def missingWords(s: str, t: str) -> str:
        # thoughts
        # use spilt to turn two strings into array of words
        # use two pointer to go through both arrays and remove the same item
        wordsInS = s.split()
        wordsInT = t.split()

        left, right = 0, 0
        ans = []
        while left < len(wordsInS) and right < len(wordsInT):
            if  wordsInS[left] == wordsInT[right]:
                left += 1
                right += 1
            else:
                ans.append(wordsInS[left])
                left += 1
        return " ".join(ans)
            