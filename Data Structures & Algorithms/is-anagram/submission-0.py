'''
Given: two strings s and t
- return true if the two strings are anagrams of each other, otherwise return false.

s and t are anagrams if:
- they contain the same characters, with each character appearing the same number of times, regardless of order
- So - duplicates COUNT  aa != a
  - > it follows that length MUST be exactly equal
- but order does NOT matter: acbb = bcab

Constraints
- 1 <= s.length, t.length <= 5 * 10^4
- strings are never empty
- strings are medium length
- s and t consist of lowercase English letters ONLY - no normalization


Approach
- iterate over all M + N (both chars both strings) O(M + N)
- add each char to a counting map for each string O(1) operation
- {'a': 2, 'b': 1} etc
- Compare pass over both of those maps O(M + N)

M must == N, so O(N) operation
'''

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_counts = Counter()
        for n in s:
            s_counts[n] += 1
        
        m_counts = Counter()
        for m in t:
            m_counts[m] += 1
        
        for s_char in s_counts.keys():
            if not m_counts[s_char] or s_counts[s_char] != m_counts[s_char]:
                return False
        
        return True

