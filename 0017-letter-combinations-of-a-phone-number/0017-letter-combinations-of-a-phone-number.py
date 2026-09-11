class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_set = {
            "2": "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ans = []
        def backtrack(digits):
            if digits == "":
                return [""]
            res = []
            element = backtrack(digits[1:])
            for i in hash_set[digits[0]]:
                for j in element:
                    res.append(i+j)
            return res
        ans = backtrack(digits)
        return ans