class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_sum = 0
        n_prod = 1
        for i in str(n):
            d = int(i)
            n_sum += d
            n_prod *= d
        return n_prod - n_sum