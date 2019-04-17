"""
Requirement:

Determine the maximum profit by making one transaction on a share ie buy once and sell later.

Algorithm:

a) Iterate through the array
b) Curr profit at i = prices[i] - min_price, where min_price is the minimum price from 0 to i-1.
c) Max profit at i = max(max_profit, curr_profit), where max_profit is the maximum profit from 0 to i-1

Complexity:

Time: O(n), Space : O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profit = float('inf'), 0

        for price in prices:
        	max_profit = max(max_profit, price-min_price)
        	min_price = min(price, min_price)

        return max_profit

print Solution().maxProfit([])
