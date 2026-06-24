class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.kv_store:
            values = self.kv_store[key]
            if(values[0][1] > timestamp):
                return ""
            elif(values[-1][1] <= timestamp):
                return values[-1][0]
            i = 0
            j = len(values)-1
            while(i <= j):
                mid = i + ((j-i)//2)
                if values[mid][1] == timestamp:
                    return values[mid][0]
                elif values[mid][1] < timestamp:
                    i = mid + 1
                else:
                    j = mid - 1
            if(values[mid][1] > timestamp):
                return values[mid-1][0]
            return values[mid][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)