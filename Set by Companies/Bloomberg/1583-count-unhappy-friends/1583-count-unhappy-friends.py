class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        thoughts:
        the questions is not very clear, I want to state it again and
        can you please help me confirm I understand correctly
        We have a bunch of people here, and the preferences[i] tells
        me who this i-th person connected, and its in order of 
        preference.
        [[friend_2_idx, firend_3_idx...], [friend_1_idx,...],...]
          ^                                 ^
        friend_1's circle,                  friend_2's circle
        And since we all have our own preferences, their might be
        unhappiness between friends because
        firend1 and friend_2 are pairs, while friend_10, and friend_5
        are pairs
        that firend_1 prefers firend_10 over friend_2
        while firend_10 prefers friend_1 over friend_5
        Oh ok it feels like a relationship problem.
        since it sounds like a graph of paired ones and we need to 
        visit all of their connected nodes. I want to create 
        it with a adj_list using dictionary.

        Then we put in the preference order for the paired ones
        So later when we compare we can have direct access.
        preference_map[i][j] means the preference order of i toward j
        """
        adj = {}
        for i, j in pairs:
            adj[i] = j
            adj[j] = i
        preference_map = [[0] * n for _ in range(n)]
        for i in range(n):
            k = n
            for j in range(len(preferences[i])):
                preference_map[i][preferences[i][j]] = k; 
                k -= 1   # k-th order of preference (highest preference on the left, lowest preference on the right)
        count = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if preference_map[i][j] > preference_map[i][adj[i]] and preference_map[j][i] > preference_map[j][adj[j]]:  # i prefers j over i's adjacent pair and j prefers i over j's adjacent pair
                    count += 1
                    break                      # 🎯 i-th unhappy friend found
        return count