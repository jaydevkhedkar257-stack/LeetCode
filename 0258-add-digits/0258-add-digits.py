class Solution:
    def addDigits(self, num: int) -> int:
        snum = str(num)
        sum = 0
        while int(snum) > 9:
            for i in snum:
                sum += int(i)
            snum = str(sum)
            sum = 0
        return int(snum)