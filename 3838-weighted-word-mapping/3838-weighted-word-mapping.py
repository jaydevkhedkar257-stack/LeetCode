class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        sum = 0
        for word in words:
            for i in word:
                sum += weights[ord(i)-ord('a')]
            res += chr(25-(sum%26)+ord('a'))
            sum = 0
        return res
        