class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0
        for i in sentences:
            temp = i.split()
            max_words = max(len(temp), max_words)
        return max_words