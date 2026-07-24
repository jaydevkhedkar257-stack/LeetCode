class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary_n = bin(n)[2:]
        # res = 0
        # for i in binary_n:
        #     if  i == "1":
        #         res += 1

        # binary_n = "+".join(bin(n)[2:])
        # rese = eval(binary_n)

        # fastest
        res = n.bit_count()
        return res