class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums == []): return 0
        sorted_nums = sorted(nums)
        prev = sorted_nums[0]
        count = 1
        max_list = [0]*len(sorted_nums)
        for i in range(1,len(sorted_nums)):
            if(sorted_nums[i] - prev == 1):
                count += 1
            elif(sorted_nums[i] - prev != 1 and sorted_nums[i] - prev != 0):
                max_list[i] = count
                count = 1
            prev = sorted_nums[i]
        max_list.append(count)
        return max(max_list)