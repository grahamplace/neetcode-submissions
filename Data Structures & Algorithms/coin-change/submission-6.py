class Solution:

    def dfs(self, coins: list[int], coins_index: int, target_amount: int, coins_taken: int, cache: dict[tuple[int, int, int], int | float]) -> int | float:
        cache_key = (coins_index, target_amount, coins_taken)

        if cache_key in cache:
            return cache[cache_key]

        if target_amount == 0:
            return coins_taken

        if coins_index >= len(coins):
            return float('inf')

        # if our largest coin is > taget, we can't "take", only skip and use current value
        if coins[coins_index] > target_amount:
            return self.dfs(coins, coins_index + 1, target_amount, coins_taken, cache)

        # take this coin
        take_result = 1 + self.dfs(coins, coins_index, target_amount - coins[coins_index], coins_taken, cache)

        # otherwise, we have two choices:
        # skip this coin
        skip_result = self.dfs(coins, coins_index + 1, target_amount, coins_taken, cache)



        result = min(skip_result, take_result)
        cache[cache_key] = result
        return result 

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        res = self.dfs(coins, 0, amount, 0, {})
        if res == float('inf'):
            return -1
        else:
            return res