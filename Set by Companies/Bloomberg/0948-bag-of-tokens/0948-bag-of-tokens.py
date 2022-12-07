class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Thoughts:
        Sounds like a stratgical game that we need to 
        decide when to take which step
        But no matter what, harder problems are consist
        of smaller problems.
        Let's look at the best token we can choose when
        we deicded to play one step.
        that if we play face up token,
        we play against the smallest value
        Else playing face down token, play with the largest
        value.
        So that I can play greedy
        two pointer will do the job
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
            