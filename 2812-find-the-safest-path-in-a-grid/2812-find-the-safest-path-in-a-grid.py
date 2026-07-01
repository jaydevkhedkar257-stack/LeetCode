import heapq
from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If the start or end cell contains a thief, the safeness factor is 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-Source BFS to compute minimum distance to any thief for each cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Step 2: Use Max-Heap (Dijkstra) to find the path maximizing the minimum safeness factor
        # Python's heapq is a min-heap by default, so we store negative values to simulate a max-heap
        max_heap = [(-dist[0][0], 0, 0)]  # (negated_safeness, r, c)
        
        # Track max safeness factor seen for each cell during path search
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist[0][0]
        
        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            d = -d  # Convert back to positive safeness
            
            # If we reached the bottom-right corner, this is our maximum possible safeness factor
            if r == n - 1 and c == n - 1:
                return d
                
            # If we found a path to this cell with a lower safeness than already processed, skip it
            if d < max_safeness[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The safeness of the path to the neighbor is limited by the minimum 
                    # safeness encountered so far or the neighbor's own distance to a thief
                    next_safeness = min(d, dist[nr][nc])
                    
                    if next_safeness > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = next_safeness
                        heapq.heappush(max_heap, (-next_safeness, nr, nc))
                        
        return 0