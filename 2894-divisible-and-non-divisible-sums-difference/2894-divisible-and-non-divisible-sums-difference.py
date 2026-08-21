class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of all numbers 1 to n
        total = n * (n + 1) // 2
        # Sum of multiples of m up to n
        k = n // m
        multiples_sum = m * k * (k + 1) // 2
        return total - 2 * multiples_sum