class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.s_nums = sorted(nums)
        self.k = k
    def add(self, val: int) -> int:
        def add_val(arr, val):
            i = 0
            j = len(arr)
            while i < j:
                mid = (i + j) // 2
                if arr[mid] < val:
                    i = mid + 1
                else:
                    j = mid
            arr.insert(i, val)
        add_val(self.s_nums, val)
        return self.s_nums[-1*(self.k)]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)