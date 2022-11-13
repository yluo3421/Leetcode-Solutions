class UnionFind:
    def __init__(self):
        # parent id => neighbor id
        # 代表parent和neighbor在同一个集合里，parent是neighbor所在集合的首领
        # 这里parent未必具有parent的真正定义，只是方便并查集定义
        self.parent_dict = {}
        self.size_of_set = {}
        self.num_of_set = 0
    
    # 链接x 和y，就是合并x和y所在的集合
    def union(self, x, y):
        #找到x和y的首领，并且合并首领
        root_x = self.find(x)
        root_y = self.find(y)
        # 如果首领不同，合并集合
        if (root_x != root_y):
            # 把root_x的set合并到root_y的set，root_y成为两个set合并之后的首领
            # 这里是自己定义的x合并到y或者y合并到x

            self.parent_dict[root_x] = root_y
            self.num_of_set -= 1
            # 更新root_y的size，这里root_x的size需要更新吗？
            self.size_of_set[root_y] += self.size_of_set[root_x]
    
    # O(1)
    def find(self, x):
        root = x
        # 一层一层找到x的最终首领
        # 最终首领在map中对应None
        while self.parent_dict[root] != None:
            root = self.parent_dict[root]
        
        # 如果x不是最终首领，将x到root的路径上所有点进行path compression
        # 压缩前 3 -> 2, 2 -> 1, 1 -> None
        # 压缩后 3 -> 1, 2 -> 1, 1 -> None
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
        if (x not in self.size_of_set):
            return 0
        return self.size_of_set[self.find(x)]