class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {
            "a" : 0,
            "e" : 0,
            "i" : 0,
            "o" : 0,
            "u" : 0
        }
        consonant = {}

        for i in s:
            if i in vowel:
                vowel[i] += 1
            else:
                consonant[i] = 1 + consonant.get(i, 0)
        maxV = max(vowel.values()) if vowel.values() else 0
        maxC = max(consonant.values())if consonant.values() else 0
        return maxV + maxC
            