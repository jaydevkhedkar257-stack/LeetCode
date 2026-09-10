class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check_set = defaultdict()
        for i in nums:
            if i in check_set:
                check_set[i] += 1
            else:
                check_set[i] = 1
        max = 0
        max_element = 0
        for i in check_set:
            if check_set[i] >= max:
                max_element = i
                max = check_set[i]
        return max_element

