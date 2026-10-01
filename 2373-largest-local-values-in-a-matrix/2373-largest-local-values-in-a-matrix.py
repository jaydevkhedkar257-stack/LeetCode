class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        res = []
        i = 0

        while i + 3 <= len(grid):
            temp = []
            j = 0
            while j + 3 <= len(grid[0]):
                chunks = grid[i:i+3]
                local_max = 0
                for chunk in chunks:
                    local_max = max(local_max, max(chunk[j:j+3]))
                temp.append(local_max)
                j += 1
            res.append(temp)
            i += 1
        
        return res
                