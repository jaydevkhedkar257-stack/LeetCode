class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        hashset = set()
        ROW = len(grid)
        COL = len(grid[0])
        max_island = 0

        def backtrack(r, c, curr):
            if min(r, c) < 0 or r >= ROW or c >= COL or (r, c) in hashset or grid[r][c] == 0:
                return []
            if grid[r][c] == 1:
                hashset.add((r, c))
                curr.append((r, c))
                backtrack(r, c + 1, curr)
                backtrack(r, c - 1, curr)
                backtrack(r + 1, c, curr)
                backtrack(r - 1, c, curr)
            return curr
        
        for i in range(ROW):
            for j in range(COL):
                if (i, j) in hashset or grid[i][j] == 0:
                    continue
                temp = backtrack(i , j, [])
                max_island = max(max_island, len(temp))
        return max_island