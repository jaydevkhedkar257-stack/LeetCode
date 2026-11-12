class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        def dist(x, y, i, j):
            return ((x-i)**2 + (y-j)**2)
        ans = [0]*len(queries)

        for k in range(len(queries)):
            x, y, r = queries[k]
            for i, j in points:
                if dist(x,y,i,j) <= r**2:
                    ans[k] += 1
        
        return ans