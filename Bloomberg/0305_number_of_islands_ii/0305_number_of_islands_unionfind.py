class UnionFind:
    def __init__(self):
        self.parent_dict = {}
        self.size_of_set = {}
        self.num_of_set = 0

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent_dict[root_x] = root_y
            self.num_of_set -= 1
            self.size_of_set[root_y] += self.size_of_set[root_x]
    
    def find(self, x):
        root = x
        while self.parent_dict[root] != None:
            root = self.parent_dict[root]
        
        while x != root:
            x_parent = self.parent_dict[x]
            self.parent_dict[x] = root
            x = x_parent
        return root
    
    def add(self, x):
        if x in self.parent_dict:
            return 
        self.parent_dict[x] = None
        self.size_of_set[x] = 1
        self.num_of_set += 1
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_num_of_set(self):
        return self.num_of_set
    
    def get_size_of_set(self, x):
        if x not in self.size_of_set:
            return 0
        return self.size_of_set[self.find(x)]

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # brutal force 
        # every time find number of islands 
        # this will be k * m * n where k is length of positions
        # Union find is the solution
        # if there is no position retrun empty
        # for each opeartion
        # we check if the location is land already
        # if it is, ans.append(curr num of set)
        # go to next positions
        # else
        # add the curr location to is land
        # add curr location to unionfind
        # start checking neighbors of curr locatin
        # if its valid, union the curr location with neighbor
        # add to ans

        if not positions:
            return []
    
        uf = UnionFind()
        is_land = set()
        num_of_islands = []
        DIRECTIONS = [(0,1), (0, -1), (-1, 0), (1, 0)]

        for position in positions:
            curr_x, curr_y = position[0], position[1]
            if (curr_x, curr_y) in is_land:
                num_of_islands.append(uf.get_num_of_set())
                continue
            uf.add((curr_x, curr_y))
            is_land.add((curr_x, curr_y))
            for direction in DIRECTIONS:
                neighbor_x = curr_x + direction[0]
                neighbor_y = curr_y + direction[1]
                if self.is_valid(neighbor_x, neighbor_y, m , n, is_land):
                    uf.union((curr_x, curr_y), (neighbor_x, neighbor_y))
            num_of_islands.append(uf.get_num_of_set())
        return num_of_islands
    def is_valid(self, neighbor_x, neighbor_y, m, n, is_land):
        if (neighbor_x, neighbor_y) not in is_land:
            return False
        if neighbor_x not in range(m) and neighbor_y not in range(n):
            return False
        return True
