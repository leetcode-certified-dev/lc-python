import math
from typing import List

"""
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) == 0:
            return 0

        if 2 * k > len(prices):
            profit = 0
            for i in range(1, len(prices)):
                profit += max(0, prices[i] - prices[i-1])
            return profit

        # dp[days][transactions][is_stock_on_hold]
        dp = [[[-math.inf] * 2 for _ in range(k+1)] for _ in range(len(prices))]
        # init condition
        dp[0][0][0], dp[0][1][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        max_profit = max(dp[len(prices)-1][j][0] for j in range(k+1))

        return max_profit
