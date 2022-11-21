from typing import (
    List,
)

class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    monotonic queue
    """
    def shortest_subarray(self, a: List[int], k: int) -> int:
        # Write your code here.
        queue = collections.deque([0])
        prefix_sum = self.get_prefix_sum(a)
        min_length = float("inf")

        for i in range(len(prefix_sum)):
            # 如果前i个数的前缀和 - queue左端的前缀和 >= k
            # 则是满足条件的可行解，用可行解的长度更新最小长度
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_length = min(min_length, i - queue.popleft())
            # 淘汰没有用的队列末尾的数字
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            # i可能是后面会用到的一个区间点，加入队列
            queue.append(i)
        
        return -1 if min_length == float("inf") else min_length

    def get_prefix_sum(self, A):
        prefix_sum = [0]
        for n in A:
            prefix_sum.append(prefix_sum[-1] + n)
        return prefix_sum