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
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        # for s in strs:
        #     key = ''.join(sorted([c for c in s]))
        #     groups[key].append(s)
        
        # return [v for _, v in groups.items()]

        # Key idea: each string can be represented by a counts tuple of size 26 (lowercase english letters only)
        groups = defaultdict(list)
        for s in strs: # O(n)
            count_key = [0 for _ in range(26)]
            for c in s: # O(100)
                count_key[ord(c) - ord('a')] += 1 # normalize 'a' to 0 
            
            groups[tuple(count_key)].append(s)
        
        return list(groups.values())
        
        

        