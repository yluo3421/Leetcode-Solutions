import heapq
class MedianFinder:
    
    def __init__(self):
        # thoughts:
        
        # array   1 2
        # minheap 1
        # maxheap
        #  1,2,3,4,5,6,7,8
        #        ^ ^
        # len(maxheap)=3 len(minheap)=4
        # return maxheap[0] should be the median
        
        # two heap constructed
        # when we add number, find rules to add to either minheap or maxheap
        # Once both heaps are ready
        # we need rules to find median using two heaps
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        # default put into minHeap      
        # minHeap ,10,11,12
        # maxHeap -1,-2,-4,-9 
        # essentially a minheap, all numbers are negative
        # the min is the max in its positive value
        # [1,9,10,2,11,12,3]
        # if curr > minHeap[0]:
        #  check len(minHeap) >= len(maxHeap) + 1:
        #       pop min from Heap, insert it to the maxHeap
        #       then add the new number to minHeap
        # check len(maxHeap) >= len(minHeap) + 1:
        #           do the pop and insert
        # if len(self.minHeap) == len(self.maxHeap):
        #     heapq.heappush(self.minHeap, num)
        # else:
        #     if num >= self.minHeap[0]:
        #         if len(self.minHeap) >= len(self.maxHeap) + 1:
        #             temp = heapq.heappop(self.minHeap)
        #             heapq.heappush(self.maxHeap, -1 * temp)
        #             heapq.heappush(self.minHeap, num)
        #         else:
        #             heapq.heappush(self.minHeap, num)
        #     else:
        #         if len(self.maxHeap) >= len(self.minHeap) + 1:
        #             temp = -1 * heapq.heappop(self.maxHeap)
        #             heapq.heappush(self.minHeap, temp)
        #             heapq.heappush(self.maxHeap, -1 * num)
        #         else:
        #             heapq.heappush(self.maxHeap, -1 * num)
        
        # minHeap -1,-3
        # maxHeap -2,
        # array -1, -2,-3
        # median -1.5
        heapq.heappush(self.minHeap, num)
        if self.minHeap and self.maxHeap and num < self.maxHeap[0] * -1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * temp)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * temp)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            temp = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
            
#         print("current minHeap")
#         print(self.minHeap)
#         print("current maxheap")
#         print(self.maxHeap)
  
    def findMedian(self) -> float:
        # minHeap 2 10
        # maxHeap 1
        # array = [1,2,10,3]
        
        # if len(minHeap) == len(maxHeap)
        # median = (minHeap[0] + maxHeap[0]) / 2
        # else
        # grab 0th element from the longer heap
        # return min/maxheap[0]
        if len(self.minHeap) == len(self.maxHeap):
            # print(self.minHeap[0])
            # print(self.maxHeap[0])
            median = (self.minHeap[0] + -1 * self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            median = self.minHeap[0]
        else:
            median = -1 * self.maxHeap[0]
        return median
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()