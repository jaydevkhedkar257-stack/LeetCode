class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Calculate nCr
        # total_ways = math.comb(n, k)
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                val = math.comb(i, j)
                temp.append(val)
            res.append(temp)
        return res


