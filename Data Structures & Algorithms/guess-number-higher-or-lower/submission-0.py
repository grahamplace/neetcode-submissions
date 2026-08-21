# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def _search_range(self, low, high):
        mid = (low + high) // 2
        if guess(mid) == -1: 
            return self._search_range(low, mid - 1)
        elif guess(mid) == 1:
            return self._search_range(mid + 1, high)
        else: 
            return mid

    def guessNumber(self, n: int) -> int:
        return self._search_range(0, n)