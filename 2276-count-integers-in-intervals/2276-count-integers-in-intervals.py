class CountIntervals:

    def __init__(self):
        self.boundary_cnt = defaultdict(int)
        self.cur_res = -1
        
    def add(self, left: int, right: int) -> None:
        self.boundary_cnt[left] += 1
        self.boundary_cnt[right + 1] -= 1
        self.cur_res = -1
        
    def count(self) -> int:
        if not self.boundary_cnt:
            return 0
        if self.cur_res != -1:
            return self.cur_res
        
        res = 0
        values = sorted(self.boundary_cnt.keys())
        left = -1
        cur_sum = 0

        for v in values:
            if v not in self.boundary_cnt:
                continue
            
            cur_sum += self.boundary_cnt[v]
            if left == -1:
                if cur_sum > 0:
                    left = v
                continue
                
            if cur_sum > 0:
                del self.boundary_cnt[v]
            else:
                right = v
                res += right - left 
                self.boundary_cnt[v] = - self.boundary_cnt[left]
                left = -1

        self.cur_res = res
        return res

    


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()