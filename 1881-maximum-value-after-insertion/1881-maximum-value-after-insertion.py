class Solution:
    def maxValue(self, n: str, x: int) -> str:
        check = (lambda i: str(x) > n[i]) if n[0] != "-" else (lambda i: str(x) < n[i])
        for i in range(len(n)):
            if check(i):
                break
        else:
            i = len(n)
        return n[:i] + str(x) + n[i:]