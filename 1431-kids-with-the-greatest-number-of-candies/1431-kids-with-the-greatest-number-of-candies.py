class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        res = [False for _ in range(len(candies))]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res[i] = True
        return res