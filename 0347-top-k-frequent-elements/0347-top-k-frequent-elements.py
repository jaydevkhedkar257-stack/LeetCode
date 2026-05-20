class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies automatically
        counts = Counter(nums)

        # 2. Grab the 'k' most common. 
        # .most_common(k) returns pairs like [(num, count), (num, count)]
        # We use a quick list comprehension to extract just the numbers.
        return [item[0] for item in counts.most_common(k)]
