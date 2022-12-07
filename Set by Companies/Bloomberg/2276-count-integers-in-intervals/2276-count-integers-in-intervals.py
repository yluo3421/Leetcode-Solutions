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

    
"""
bisect and array
 bisect_left(list, num, beg, end) :- This function returns 
 the position in the sorted list, where the number passed in 
 argument can be placed so as to maintain the resultant list 
 in sorted order. If the element is already present in the list, 
 the leftmost position where element has to be inserted is returned. 

This function takes 4 arguments, list which has to be worked with, 
number to insert, starting position in list to consider, ending 
position which has to be considered. 
"""
class CountIntervals:

    def __init__(self):
        self.arr = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        pos = bisect_left(self.arr, (left, right))
        if pos > 0: pos-=1
        while pos<len(self.arr):
            if left>self.arr[pos][1]:
                pos+=1
                continue
            if self.arr[pos][0]>right: break
            left = min(left, self.arr[pos][0])
            right = max(right, self.arr[pos][1])
            removed = self.arr.pop(pos)
            self.cnt-=removed[1]-removed[0]+1
        self.arr.insert(pos, (left, right))  
        self.cnt+=right-left+1

    def count(self) -> int:
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()