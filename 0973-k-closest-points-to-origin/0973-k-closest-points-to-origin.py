class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        arr = []
        res = []
        for i in range(len(points)):
            d = points[i][0]**2 + points[i][1]**2
            arr.append((d,i))       
        heapq.heapify(arr)
        for _ in range(k):
            element = heapq.heappop(arr)
            res.append(points[element[1]])
        
        return res