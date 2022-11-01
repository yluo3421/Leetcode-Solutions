import heapq
class MedianFinder:
    
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if self.minHeap and self.maxHeap and num < (-1 * self.maxHeap[0]):
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * temp)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * temp)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            temp = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * temp)
        
  
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0] * -1) / 2
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0] * -1
        else:
            return self.minHeap[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()