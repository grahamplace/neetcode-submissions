class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        # when 3 steps away, solution is 1 + solution(2)
        # f(3) = 1 + f(2)
        # when 4 away, could take 1 step and have f(3) options, or two steps and have f(2) options
        # f(4) = 1 + f(3) + 1 + f(2)
        # f(5) = take two steps + f(3), or 1 step + f(4)
        # bottom up DP: base case first, then store last two (since can only take two steps)
        dp = [2, 3]

        i = 4
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1

        return dp[1]
