class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        arr = [i*-1 for i in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            y = heapq.heappop(arr) * -1
            x = heapq.heappop(arr) * -1
            if x != y:
                heapq.heappush(arr,(y-x)*-1)
        
        return arr[0]*-1 if arr else 0
