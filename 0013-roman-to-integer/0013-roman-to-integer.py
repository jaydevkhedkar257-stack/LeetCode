class Solution:
    def romanToInt(self, s: str) -> int:
        Symbolval = {"I" :1, "V" :5, "X" :10, "L" :50, "C" :100, "D" :500, "M" :1000}
        num = 0
        prev = 0
        for i in range(len(s)-1,-1,-1):
            if(prev > Symbolval[s[i]]):
                num -= Symbolval[s[i]]
            else:
                num += Symbolval[s[i]]
            prev = Symbolval[s[i]]
        return num