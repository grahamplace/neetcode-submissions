from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        
        left, max_seen = 0, 0
        counts = Counter() # max O(26) size

        for right, char in enumerate(s):
            counts[char] += 1
            substr_len = (right - left + 1)
            is_valid = (substr_len - counts.most_common(1)[0][1]) <= k
            if is_valid:
                max_seen = max(max_seen, substr_len)
            else:
                counts[s[left]] -= 1
                left += 1

        return max_seen
