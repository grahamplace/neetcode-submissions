'''
INPUTS 
nums:
- int array
- nums is always non-empty
- num elems can be negative


k:
- int
- "k most frequent values in nums"
- k is never > the number of distinct elems in nums (impossible to answer)


EXAMPLE
in: [1,2,2,3,3,3], k = 2
out: [2,3]

in: [7,7], k = 1
out: [7]

BRUTE FORCE
- iterate over nums
- for each, incr a Counter value
- sort Counter by values DESC
- return k keys
- O(n) to fill up counter
- O(mlogm) to sort, where m is the number of DISTINCT values in nums. could be n worst case

IDEA
- keep a data structure of size k (ordereddict?)
- this is the top k elements and their counts
- Single pass over nums
- if we encounter a num where the new count exceeds the old min count, we should replace it 

'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return sorted(c, key=lambda x: c[x], reverse=True)[:k]
        