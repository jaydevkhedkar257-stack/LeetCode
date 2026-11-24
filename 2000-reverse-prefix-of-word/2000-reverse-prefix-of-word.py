class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        indx = 0
        for i in range(len(word)):
            if word[i] == ch:
                indx = i
                break
        res = word[0:indx+1][::-1] + word[indx+1::]
        return res