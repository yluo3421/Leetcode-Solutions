"""
這題沒有python解, 所以分享一下我的解答
主要的考點有三個

BFS: 沒什麼好說的 number of distinct island刷一下, 用deque實踐, Time:O(N), Space: O(islands)
Rotation/Flip: 大概知道一下rotation的兩步翻轉怎麼做, 先換ij, 再reverse, 不熟悉的同學可以看一下rotate image這題
選代表: 如老師上課提到的,當有很多可能的時候可以用選代表簡化可能性
我的做法是, 首先用BFS把所有的島嶼找到,接著因為知道Rotation+Flip最多可能有八種可能,
所以在子函數中做Flip跟Rotation, 把island座標轉成tuple用list存起來,
最後sort選出最小序的tuple當代表, 存進set裡去重

註一：在這裡如果對python不熟悉的同學可能會有點疑惑為什麼要轉成tuple再扔進set,
主要的原因是python set(hashtable)裡只能存immutable的東西, 像是string, tuple或int
所以必須對island這個list of list做轉換才能放入set(hashtable)裡, dictionary的key也是一樣的情況
註二：為什麼用選代表？
一個直覺是, 像2x2形狀的island可能Flip跟Rotation長一樣(ex: [[0,0],[0,1],[1,0]]),
換句話說不是每種形狀都有八種可能, 這時候列舉全部來除8可能會出錯, 所以選代表是比較安全也更簡單的做法
"""
from collections import deque, defaultdict
class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        # 1. use BFS to find all islands
        row, col = len(grid), len(grid[0])
        visited = set([])
        delta = [(-1,0),(1,0),(0,1),(0,-1)]
        islands = []
        for r in range(row):
            for c in range(col):
                min_r, min_c = row, col
                if grid[r][c] == 1 and (r, c) not in visited:
                    min_r, min_c = min(min_r, r), min(min_c, c)
                    visited.add((r, c))
                    island = [[r, c]]
                    dq = deque([ [r, c] ])
                    while dq:
                        curr_r, curr_c = dq.popleft()
                        for dr, dc in delta:
                            new_r, new_c = curr_r + dr, curr_c + dc
                            if not (0 <= new_r <= row - 1 and 0 <= new_c <= col - 1):
                                continue
                            if grid[new_r][new_c] != 1 or (new_r, new_c) in visited:
                                continue
                            visited.add((new_r, new_c))
                            min_r, min_c = min(min_r, new_r), min(min_c, new_c)
                            dq.append([new_r, new_c])
                            island.append([new_r, new_c])
                    # 2. Normalize: shift island to (0,0)
                    for index in range(len(island)):
                        island[index][0] -= min_r
                        island[index][1] -= min_c
                    island.sort()
                    islands.append(island)
        # 3. Find representation and count result
        return self.count_unique_islands(islands)
    def count_unique_islands(self, islands):
        s = set([])
        for island in islands:
            s.add(self.find_represent(island))
        return len(s)
    def find_represent(self, island):
        result = []
        result.append(self.convert_island_to_tuple(island))
        result.append(self.convert_island_to_tuple(self.flip(island)))
        rotation = self.rotate(island)
        for _ in range(3):
            result.append(self.convert_island_to_tuple(rotation))
            result.append(self.convert_island_to_tuple(self.flip(rotation)))
            rotation = self.rotate(rotation)        
        result.sort()
        return result[0]
    def rotate(self, island):
        new_island = []
        max_r, max_c = 0, 0
        for pair in island:
            max_r = max(max_r, pair[0])
            max_c = max(max_c, pair[1])
        for pair in island:
            new_island.append([pair[1], max_r - pair[0]])
        new_island.sort()
        return new_island
    def convert_island_to_tuple(self, island):
        result = []
        for pair in island:
            result.extend(pair)
        return tuple(result)
    def flip(self, island):
        new_island = []
        max_r, max_c = 0, 0
        min_r, min_c = float('inf'), float('inf')
        for r, c in island:
            max_r, max_c = max(max_r, r), max(max_c, c)
            min_r, min_c = min(min_r, r), min(min_c, c)
        for r, c in island:
            new_island.append([r - min_r, max_c - c - min_c])
        new_island.sort()
        return new_island