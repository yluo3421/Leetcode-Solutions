from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: An integer
    """
    def jump(self, a: List[int]) -> int:
        # write your code here
        # Greedy
        rightMost = 0
        end = 0
        step = 0
        for i in range(len(a) - 1):
            rightMost = max(i + a[i], rightMost)
            if i == end:
                step += 1
                end = rightMost
        return step

        # DP
        n = len(a)
        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + a[j] >= i:
                    dp[i] = min(dp[j] + 1, dp[i])
                    break
        return dp[n - 1]
"""
贪心法
解题思路
我们利用贪心思想，实时维护最远可达的位置rightmost，和上次起跳点能到达的最远边界end。step是跳跃次数，即最终的返回结果。

依次遍历每个位置i，以i作为起跳点，假设这是第step次跳跃，已知第step-1次跳跃时能跳到的最远距离是end

首先更新rightmost = max(rightmost, A[i] + i)，实时更新能跳到的最远的位置。

如果end == i，说明已经到达了第step-1次跳跃时能跳到的边界，跳跃次数step就加1，end更新为rightmost作为下个边界。

跳到终点后，返回跳跃次数step。

举例分析
以A = [2, 3, 1, 1, 4]为例。

i = 0时，以A[0]为起跳点，最远能跳到第rightmost = 2个位置。因为end == i，所以跳的次数加1，step为1。同时，end更新为2，表明下次跳跃的边界。

i = 1时，更新rightmost = 1 + A[1] = 4。

i = 2时，最远位置rightmost没有被更新。因为end == i，说明到达边界，所以跳的次数加1，step为2。

i = 3时，最远位置rightmost没有被更新。

到达A[4]，遍历结束，最终结果step为2。

复杂度分析
时间复杂度：O(n)O(n)，n为数组长度。一次遍历。

空间复杂度：O(1)O(1)。
"""
