class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv_store.get(key)
        if not values:
            return ""
        i, j = 0, len(values) - 1
        ans = ""
        while i <= j:
            mid = (i + j) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                i = mid + 1
            else:
                j = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)