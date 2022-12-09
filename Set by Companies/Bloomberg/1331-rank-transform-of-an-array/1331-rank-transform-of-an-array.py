class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for a in sorted(arr):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, arr)