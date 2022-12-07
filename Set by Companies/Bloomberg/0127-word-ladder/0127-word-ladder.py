class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        With the example 1
        hit - hot - dot - dog - log
                    lot         cog
             
        The idea is to use bfs and find the next step words
        and keep searching until the endWord found.
        To efficiently find the intermediate nodes that is
        differ by one letter, we need to do some pre-move
        on wordList.
        Assume we already have the dicitoanry of pre-processed
        wordList, this way we can access it by O(1)
        We use a tuple of beginWord and 1, 1 represents level
        of search, this way we can find the shortest path
        Visited set needed to avoid loop
        With BFS and queue, we take the first element in queue
        curr_word
        find all its transformation and find out its next steps
        and add them to queue with level + 1
        Eventually found the endWord and return path length
        Time O(n^2 * k) n length of word, k is total number of words in input wordList
        Space O(n^2 * k)
        """
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0
        
        n = len(beginWord)
        # build the map of intermediate word
        adjacent_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                adjacent_dict[word[:i] + "*" + word[i + 1:]].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(n):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in adjacent_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                adjacent_dict[intermediate_word] = []
        return 0
        
"""
        Double BFS
        The algorithm is very similar to the standard BFS based approach we saw earlier.

The only difference is we now do BFS starting two nodes instead of one. 
This also changes the termination condition of our search.

We now have two visited dictionaries to keep track of nodes visited from 
the search starting at the respective ends.

If we ever find a node/word which is in the visited dictionary of the 
parallel search we terminate our search, since we have found the meet point 
of this bidirectional search. It's more like meeting in the middle instead 
of going all the way through.

Termination condition for bidirectional search is finding a word which 
is already been seen by the parallel search.

The shortest transformation sequence is the sum of levels of the meet 
point node from both the ends. Thus, for every visited node we save its 
level as value in the visited dictionary.
        
        """
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in self.all_combo_dict[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)
                        
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queues for birdirectional BFS
        queue_begin = collections.deque([beginWord]) # BFS starting from beginWord
        queue_end = collections.deque([endWord]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord : 1}
        visited_end = {endWord : 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:
            
            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0





        
        
        
        
        