class MaxStack:

    def __init__(self):
        """
        Thoughts:
        the original idea of two stack is not working
        because at function popMax we are not able to do it
        in O(logn)
        instead of inside max_idx to return the current idx
        for max elemnt, maybe I can maintain a max_heap of all
        idx for this
        self.stack = [5,1,5]
        self.max_idx = [(5, [0]),(5,[0]),(5,[0,-2])]
        """
        self.stack = [] 
        self.heap = []
        self.count = 0
        self.removed = set()
        

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.count))
        self.stack.append((x, self.count))
        self.count += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, idx = self.stack.pop()
        self.removed.add(idx) # no -1 needed because we add to set
        return num
        

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]
        
    def peekMax(self) -> int:
        while self.heap and (-1 * self.heap[0][1]) in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and (-1 * self.heap[0][-1]) in self.removed:
            heapq.heappop(self.heap)
        num, idx = heapq.heappop(self.heap)
        self.removed.add(-1 * idx)
        return -1 * num
        
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()