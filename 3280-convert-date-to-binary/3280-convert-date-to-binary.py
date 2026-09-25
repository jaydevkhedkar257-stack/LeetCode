class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split("-")
        for i in range(len(arr)):
            arr[i] = bin(int(arr[i]))[2::]
        
        res = "-".join(arr)
        return res