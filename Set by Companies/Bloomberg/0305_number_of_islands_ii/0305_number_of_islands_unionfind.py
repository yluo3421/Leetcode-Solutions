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


"""
以下是不需要单独构建UnionFind的解法
每次查询代表元均摊是**O(α) α代表反阿克曼函数，反阿克曼函数是渐进增长
很慢很慢的，我们可以近似的认为每次查询是O(1)**的复杂度
我们一共有K次操作，每次操作最多并查集查询4次，并查集合并4次,所以我
们最终的时间复杂度是O(K)的

空间复杂度
n m是输入数组 的长和宽

我们需要一个fa数组大小为nm，一个vis数组（标记该
点有没有变成岛屿），所以空间复杂度是O(nm)
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    # 计算编号的函数
    def calc(self, x, y, n, m):
        return x * m + y
    # 寻找代表元的函数
    def find(self, fa, x):
        # x是代表元，直接返回
        if (x == fa[x]):
            return x
        # x不是代表元，寻找x的父亲的代表元是谁，并且直接把代表元赋值给x的父亲，进行路径压缩
        else:
            fa[x] = self.find(fa, fa[x])
            return fa[x]
    def numIslands2(self, n, m, operators):
        # write your code here
        # 父亲数组和标记点i有没有已经变成岛屿的数组
        fa = []
        visited = {}
        ans = []
        # 初始化fa数组和vis数组 和答案数组
        for i in range(n):
            for j in range(m):
                fa.append(self.calc(i, j, n, m))
                visited[self.calc(i, j, n, m)] = False
        cnt = 0
        zx = [0, 0, 1, -1]
        zy = [1, -1, 0, 0]
        for op in operators:
            x = op.x
            y = op.y
            # x y点的编号
            idx = self.calc(x, y, n, m)
            if visited[idx] != True:
                cnt += 1
                for k in range(4):
                    nx = x + zx[k]
                    ny = y + zy[k]
                    # nx ny点的编号
                    nidx = self.calc(nx, ny, n, m)
                    #  判断往四周走有没有走越界，或者走到海洋里，越界或者走到海洋都是没有的状态
                    if (nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nidx] == False):
                        continue
                    # 判断四周的岛屿是不是和当前第i次操作的岛屿 已经在一个集合了
                    # 如果不是在一个集合里，那么i j所在的两个集合就是连通的，可以合并算为一个集合,然后让岛屿数量-1。
                    # 我们只要让i所在集合的代表元改为j所在集合的代表元就完成了合并操作
                    if (self.find(fa, idx) != self.find(fa, nidx)):
                        cnt -= 1
                        fa[self.find(fa, idx)] = self.find(fa, nidx)
                # 标记它已经是个岛屿了
                visited[idx] = 1
                ans.append(cnt)
            else:
                ans.append(cnt)
        return ans