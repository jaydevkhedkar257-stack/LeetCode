class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum = (n)**2
        evensum = (n)*((n)+1)
        while evensum:
            oddsum, evensum = evensum, oddsum % evensum
        return oddsum