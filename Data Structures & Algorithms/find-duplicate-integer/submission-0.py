from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive:
        return Counter(nums).most_common(1)[0][0]