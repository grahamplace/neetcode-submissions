'''
Solution ignoring the * thing:
from os import close
from os import close

()()
every time we encounter ), we have to have a remaining ( to map it to 
()) => invalid

It's like a decision tree where when you encounter *,
you have three choices of how to treat it: ) ( or skip

At each decision fork, 
 Make one possible choice and "continue" by calling recursively the rest of the string + updated counts

if ANY of the three recursive calls are valid, then the string is valid

'''

from functools import cache

class Solution:
    # def _checkValidString(self, s: str) -> bool:
    #     open_count = 0
    #     for c in s:
    #         if c == '(':
    #             open_count += 1
    #         elif c == ')':
    #             if open_count == 0:
    #                 return False
    #             else:
    #                 open_count -= 1

    #     # if any "unused open" -> invalid
    #     return open_count == 0

    @cache
    def _checkValidString(self, s: str, open_count: int, idx: int) -> bool:
        # base case 1: end of string with unused opens
        if idx == len(s):
            return open_count == 0 # if any unused opens at end, s is invalid
        
        # base case 2: reach an invalid close paren, return early, string is invalid
        if s[idx] == ')':
            if open_count == 0:
                return False
            else: 
                return self._checkValidString(s, open_count - 1, idx + 1)
        
        if s[idx] == '(':
            return self._checkValidString(s, open_count + 1, idx + 1)
        
        if s[idx] == '*':
            # Treat it like )
            if open_count == 0:
                close_paren = False
            else:
                close_paren = self._checkValidString(s, open_count - 1, idx + 1)
            
            if close_paren: return True

            # Treat it like (
            open_paren = self._checkValidString(s, open_count + 1, idx + 1)
            if open_paren: return True

            # Treat it like skip:
            skip = self._checkValidString(s, open_count, idx + 1)
            if skip: return True

            return False # if none of the choices make a valid subprob
        
        # Should be unreachable if inputs are valid
        raise ValueError("Unexpected character")

        
    
    def checkValidString(self, s: str) -> bool:
        # assert self._checkValidString('(', 0, 0) == False
        # assert self._checkValidString(')', 0, 0) == False
        # assert self._checkValidString(')(', 0, 0) == False
        # assert self._checkValidString('()', 0, 0) == True
        # assert self._checkValidString('()()', 0, 0) == True
        # assert self._checkValidString('((()))', 0, 0) == True
        # assert self._checkValidString('(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())', 0, 0) == True
        return self._checkValidString(s, 0, 0)
        