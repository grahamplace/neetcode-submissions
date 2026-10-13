class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        q = deque(s)
        for c in t:
            if len(q) == 0: return True
            if c == q[0]:
                if len(q) > 0:
                    q.popleft()
        
        return len(q) == 0
        

