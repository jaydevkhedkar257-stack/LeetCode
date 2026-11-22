class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_sum = 0
        n_prod = 1
        while n:
            d = n%10
            n_sum += d
            n_prod *= d
            n //= 10
        return n_prod - n_sum