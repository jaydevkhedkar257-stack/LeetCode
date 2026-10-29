class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = defaultdict(list)
        res = []
        for i, s in enumerate(groupSizes):
            buckets[s].append(i)
            if len(buckets[s]) == s:
                res.append(buckets[s])
                buckets[s] = []
        return res