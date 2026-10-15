class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        n = ''.join(filter(str.isalnum, s))
        n = n.lower()
        #print(n)
        j = len(n) - 1
        while i < j:
            if n[i] != n[j]:
                return False
            i += 1
            j -= 1
        return True