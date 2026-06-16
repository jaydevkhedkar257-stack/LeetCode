class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(not s):
            return 0
        i = 0
        j = 0
        count = 0 
        while j <= len(s):
            set_s = set(s[i:j])
            list_s = list(s[i:j])
            if(len(set_s) == len(list_s)):
                j += 1
                count = max(count,len(list_s))
                # print(set_s,list_s,count,"ACCEPTED",sep = "\t")
            else:
                i += 1
                # print(set_s,list_s,count,"IGNORED",sep = "\t")
        return count