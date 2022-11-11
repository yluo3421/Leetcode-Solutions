class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # thoughts:
        # use minheap to maintain k numbers
        # every time we push in there until k
        # then we pop and push
        # minHeap []
        # array = [3,2,1,5,6,4]
        minHeap = []
        count = 0
        for num in nums:
            count += 1
            if count <= k:
                heapq.heappush(minHeap, num)
            else:
                if num < minHeap[0]:
                    continue
                else:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num)
        print(minHeap)
        return minHeap[0]
            

    