"""
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        left_min, right_max = prices[0], prices[-1]
        left_profit = [0] * length
        right_profit = [0] * (length + 1)

        for i in range(1, length):
            left_profit[i] = max(left_profit[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

            j = length-1-i
            right_profit[j] = max(right_profit[j+1], right_max - prices[j])
            right_max = max(right_max, prices[j])

        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_profit[i] + right_profit[i+1])

        return max_profit