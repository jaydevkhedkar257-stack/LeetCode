class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum())
        for i in range(len(clean)//2):
            if(clean[i].lower() != clean[len(clean)-(i+1)].lower()):
                return False
        return True