class Solution:
    # def concatenatedBinary(self, n: int) -> int:
    #     MOD = 10**9 + 7
    #     concatenation = "".join(bin(i)[2:] for i in range(n + 1))
    #     return int(concatenation, 2) % MOD

    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        length = 0  # bit length of addends
        result = 0   # long accumulator
        for i in range(1, n + 1):
            # when meets power of 2, increase the bit length
            if math.log(i, 2).is_integer():
                length += 1
            result = ((result * (2 ** length)) + i) % MOD
        return result