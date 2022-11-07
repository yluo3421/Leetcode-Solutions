from typing import (
    List,
)

class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
             we will sort your return value in output
    """
    """
        if we have N words, each word length is L
        Keep in mind that word can be used multiple times
        How many different square can we generate
        N^L, the square generated will be L^2
        that means each row we can pick N words
        Which is N^L
        We can generate all of them and check if they match
        How to improve?

        after choosing two words for first two rows
        the third row needs a word start with [0][2] and [1][2]
        We can use a hash map to store word start with certain ones
        Or we can use Trie
        
    """
    def word_squares(self, words: List[str]) -> List[List[str]]:
        # write your code here
        prefix_to_words = self.get_prefix_to_words(words)
        squares = []

        for word in words:
            self.search(prefix_to_words, [word], squares)
        return squares
    
    def get_prefix_to_words(self, words):
        prefix_to_words = {}

        # go through all words
        for word in words:
            # go through all prefix of the word
            for i in range(len(word)):
                prefix = word[:i]
                # if prefix not there, save []
                prefix_to_words.setdefault(prefix, [])
                # create the corelation of word and prefix
                prefix_to_words[prefix].append(word)
        return prefix_to_words
    
    def search(self, prefix_to_words, square, squares):
        square_row_cnt = len(square[0])
        curr_row_index = len(square)

        # exit of recrusion, if square is done, add to result array
        if curr_row_index == square_row_cnt:
            squares.append(list(square))
            return
        
        # form the curr row prefix by previous rows
        # prefix = "". join([square[i][curr_row_index] for i in range(curr_row_index)]) 
        for row_index in range(curr_row_index, square_row_cnt):
            prefix = "". join([square[i][curr_row_index] for i in range(curr_row_index)]) 
            if prefix not in prefix_to_words:
                return 

        for word in prefix_to_words.get(prefix, []):
            # add word with same prefix to current square
            square.append(word)
            self.search(prefix_to_words, square, squares)
            # backtrack, delete the previously added word
            # try other words
            square.pop()
        
"""
Further imporve by pruning
a b c d e
b w x y z
c x       10 words with prefix cx
d y       15 words with prefix dy
e z       0 words with perfix ez
So we can stop this route
"""

