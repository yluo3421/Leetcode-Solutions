class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Thoughts:
        Brutal force method, that if we play face up token,
        we play against the smallest value
        Else playing face down token, play with the largest
        value.
        two pointer
        """
        tokens.sort()
        n = len(tokens)
        left = 0
        right = n - 1
        ans = 0
        score = 0
        while left <= right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
                ans = max(ans, score)
            elif power < tokens[left] and score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                return ans
        return ans
            