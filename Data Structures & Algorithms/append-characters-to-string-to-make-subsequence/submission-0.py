class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        if len(s) == 0:
            return len(t)
        while i <= (len(s)-1) and j <= (len(t)-1):
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else: 
                i = i + 1
        return (len(t) - j)        
