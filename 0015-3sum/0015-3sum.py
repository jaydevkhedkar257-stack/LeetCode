class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        snums = sorted(nums)
        triplets = []
        for i in range(len(snums) - 1):
            if i > 0 and snums[i] == snums[i-1]:  # skip duplicate i
                continue
            j = i + 1
            k = len(snums) - 1
            while j < k:
                total = snums[i] + snums[j] + snums[k]
                if total == 0:
                    triplets.append([snums[i], snums[j], snums[k]])
                    j += 1
                    k -= 1
                    while j < k and snums[j] == snums[j-1]:  # skip duplicate j
                        j += 1
                    while j < k and snums[k] == snums[k+1]:  # skip duplicate k
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return triplets