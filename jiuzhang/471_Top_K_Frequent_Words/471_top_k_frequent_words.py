from typing import (
    List,
)

import heapq
from functools import cmp_to_key
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        p = []
        for key, value in dict.items():
            p.append((value, key))

        p.sort(key=cmp_to_key(self.cmp))
        result = []
        for i in range(k):
            result.append(p[i][1])
        return result

    def cmp(self, a, b):
        if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
            return -1
        elif a[0] == b[0] and a[1] == b[1]:
            return 0
        else:
            return 1
