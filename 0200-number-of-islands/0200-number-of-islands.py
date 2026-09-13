class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        hashset = set()
        res = []
        def backtrack(r, c, curr):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in hashset:
                return []
            elif grid[r][c] == "1":
                hashset.add((r,c))
                curr.append((r,c))
                backtrack(r + 1, c, curr)
                backtrack(r - 1, c, curr)
                backtrack(r, c + 1, curr)
                backtrack(r, c - 1, curr)
            return curr
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                if (i, j) in hashset:
                    continue
                res.append(backtrack(i, j, []))
        return len(res)

            