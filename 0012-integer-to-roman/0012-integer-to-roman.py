class Solution:

    def intToRoman(self, num: int) -> str:
        res = ""
        while(num > 0):
            print(num, res)
            if(str(num)[0] == "9"):
                if(num >= 900):
                    num -= 900
                    res += "CM"
                elif(num >= 90):
                    num -= 90
                    res += "XC"
                elif(num >= 9):
                    num -= 9
                    res += "IX"
            elif(str(num)[0] == "4"):
                if(num >= 400):
                    num -= 400
                    res += "CD"
                elif(num >= 40):
                    num -= 40
                    res += "XL"
                elif(num >= 4):
                    num -= 4
                    res += "IV"
            elif(num >= 1000):
                num -= 1000
                res += "M"
            elif(num >= 500):
                num -= 500
                res += "D"
            elif(num >= 100):
                num -= 100
                res += "C"
            elif(num >= 50):
                num -= 50
                res += "L"
            elif(num >= 10):
                num -= 10
                res += "X"
            elif(num >= 5):
                num -= 5
                res += "V"
            else:
                num -= 1
                res += "I"
        return res