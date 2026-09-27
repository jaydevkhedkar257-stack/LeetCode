class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        str_start = bin(start)[2:]
        str_goal = bin(goal)[2:]
        i = -1
        count_bits = 0

        while abs(i) <= len(str_goal) and abs(i) <= len(str_start):
            if str_goal[i] != str_start[i]:
                count_bits += 1
            i -= 1

        if len(str_start) > len(str_goal):
            count_bits += str_start[:(i+1)+len(str_start)].count("1")
            
        else:
            count_bits += str_goal[:(i+1)+len(str_goal)].count("1")

        return count_bits