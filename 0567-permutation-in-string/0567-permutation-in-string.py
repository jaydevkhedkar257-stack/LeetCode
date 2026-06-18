from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        if window == need:
            return True
        
        i = 0
        for j in range(len(s1), len(s2)):
            # Add new char on right
            window[s2[j]] += 1
            # Remove old char on left
            window[s2[i]] -= 1
            if window[s2[i]] == 0:
                del window[s2[i]]  # keep Counter clean for == comparison
            i += 1
            
            if window == need:
                return True
        
        return False