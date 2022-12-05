
from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        I used to like dictionary a lot because it was the first
        different data structures I learnt other than array 
        and it is so useful. But now it doesn't look nice with aliens
        Let's see
        the first thought I have is that I can check all words ith 
        char, that will tell me some order.
        And it can only be told when the prefix are the same
        The only rule we can draw is the one based on the first difference between the two words.
        ["wrt","wrf","er","ett","rftt"]
        1st letter tells me
        [wweer] -> [w,e,r]
        2nd letter tells me
        [rr,rt,f] -> [r,t]
        3rd letter tells me
        [tf,"",t] ->[t,f]
        er, et tells me r -> t
        w -> e -> r
        This looks like a graph now, and the example 2 is self loop case
        I can use topologicial sort to find out their order and
        if at the end the sorted order output doesnt have the length
        of unique char in words, meaning there is some loop.
        
        Time O(C)
        Worst case is that in the part we find first and second word and
        check for every letter of every word
        """
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})
        
        for first_word, second_word in zip(words, words[1:]):
            for char1, char2 in zip(first_word, second_word):
                if char1 != char2:
                    if char2 not in adj_list[char1]:
                        adj_list[char1].add(char2)
                        in_degree[char2] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        
        ans = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            ans.append(c)
            for next_char in adj_list[c]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    queue.append(next_char)
        if len(ans) < len(in_degree):
            return ""
        return "".join(ans)