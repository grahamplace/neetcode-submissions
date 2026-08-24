'''
- Given an array of strings strs: 
["act","pots","tops","cat","stop","hat"]

- Group all anagrams together into sublists:
[["hat"],["act", "cat"],["stop", "pots", "tops"]]

- anagrams = same characters, in any order
- length must match
- duplicates count (aa != a)

Constraints / reqs:
- You may return the output in any order
- 1 <= strs.length <= 10000, max 10k strings in input 
- 0 <= strs[i].length <= 100, indiv. strings are relatively short 
- strs[i] is made up of lowercase English letters.

idea: 
- each string hashes into sorted letters O(100 * log(100)) for each str < 100 ln
- n of those sorts = O(n) time complexity
- space:
- hash map, keys = distinct possible sorted anagram values
- there are only 100 max of those, since strs go up to 100 len only
- each input str maps to only one key, so the combined mem of the values = O(n)
- space O(n + 100) = O(n)
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted([c for c in s]))
            groups[key].append(s)
        
        return [v for _, v in groups.items()]

        