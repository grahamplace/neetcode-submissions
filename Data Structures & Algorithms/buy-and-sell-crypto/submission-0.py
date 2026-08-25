class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_seen = 0
        for idx, buy_price in enumerate(prices):
            for j in range(idx + 1, len(prices)):
                max_seen = max(max_seen, prices[j] - buy_price)
        
        return max_seen

