class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        temp1 = s[:k][::-1]
        temp2 = s[k::]
        print(temp1)
        return temp1 + temp2