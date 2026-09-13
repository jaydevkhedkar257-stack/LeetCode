class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        hashset = set()
        for i in nums:
            if i in hashset:
                res.append(i)
            else:
                hashset.add(i)
        return res