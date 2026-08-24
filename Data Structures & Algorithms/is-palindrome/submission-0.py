'''
aba -> true
i = a, j = a 
i = b, j = b 
return True 

abba
i = a, j = a 
i = b, j = b 

- case-insensitive 
- ignores all non-alphanumeric characters
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1

        return True