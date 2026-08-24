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
        i, j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True