class Leaderboard:

    def __init__(self):
        # dict sounds like a good one to store
        # but the top function can not be easily implemented
        # we can use a min heap to store k values to implement
        self.player_score = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.player_score:
            self.player_score[playerId] = 0
        self.player_score[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for score in self.player_score.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        ans = 0
        while heap:
            ans += heapq.heappop(heap)
        return ans

    def reset(self, playerId: int) -> None:
        del self.player_score[playerId]
    
    """
    O(1)
    O(K) + O(NlogK) it takes O(K) to intialize heap
    then the next N - K items each heappop takes log(K)
    thus final O(NlogK)
    O(1)
    """

    """
    to make a better time complexity of top method
    we can use a BST to store and grab top K items
    it will make the other two methods O(logK)
    """


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)