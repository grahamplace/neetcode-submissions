class Solution:
    @staticmethod
    def solve(k, piles):
        hours = 0
        for pile in piles:
            # hours to eat this pile = ceil(pile size / k)
            hours += math.ceil(pile / k)
        
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        ans = high

        while low <= high:
            mid = (low + high) // 2
            mid_hrs = self.solve(mid, piles)

            if mid_hrs > h:
                low = mid + 1
            else:
                high = mid - 1
                ans = min(ans, mid)

        
        return ans
            