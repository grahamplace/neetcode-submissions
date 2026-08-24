class Solution:
    # Sliding Window:
    # keep a window which is ALWAYS unique only
    # if we encounter a dupe, we shrink the window until dupe is removed
    # as we change window size, we update curr max if new max seen
    # (z)xyzxyz 
    # (zx)yzxyz
    # (zxy)zxyz
    # (zxyz)xyz * 
    # z(xyz)xyz
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_seen, left, right, seen = 1, 0, 1, set([s[0]])
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_seen = max(max_seen, len(seen))
            right += 1

        return max_seen
