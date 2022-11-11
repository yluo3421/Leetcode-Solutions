from typing import (
    List,
)

class Solution:
    """
    @param arr: the steps whether have glue
    @return: the sum of the answers
    """
    def rat_jump(self, arr: List[int]) -> int:
        # Write your code here.
        n = len(arr)
        # state: dp[i][0] 代表从0的位置跳偶数步后到i的位置的方案数
        #        dp[i][1] 代表从0的位置跳奇数步后到i的位置的方案数
        # 结果位置为n - 1，只需要推导出到达非终点0, -- n - 2的方案数即可
        #之后会有专门逻辑求得到达终点的方案数
        MOD = 10**9 + 7
        dp = [[0, 0] for _ in range(n - 1)]

        dp[0][0] = 1

        even_jumps = [1,3,4]
        odd_jumps = [1,2,4]

        # 奇数跳偶数 dp[i][0] = dp[i - 1][1] + dp[i - 3][1] + dp[i - 4][1]
        # 偶数跳奇数 dp[i][1] = dp[i - 1][0] + dp[i - 2][0] + dp[i - 4][0]
        for i in range(1, n - 1):
            #如果有胶水，跳过
            if arr[i] == 1:
                continue
            #奇数跳偶数
            for jump in even_jumps:
                if i - jump >= 0:
                    dp[i][0] = (dp[i][0] + dp[i - jump][1]) % MOD
            #偶数跳奇数
            for jump in odd_jumps:
                if i - jump >= 0:
                    dp[i][1] = (dp[i][1] + dp[i - jump][0]) % MOD
        
        # ans = sum {dp里面所有可以作为倒数最后一步的位置}
        plans = 0
        for jump in even_jumps:
            for i in range(max(0, n - jump - 1), n - 1):
                plans = (plans + dp[i][1]) % MOD
        
        for jump in odd_jumps:
            for i in range(max(0, n - jump - 1), n - 1):
                plans = (plans + dp[i][0]) % MOD
        return plans

