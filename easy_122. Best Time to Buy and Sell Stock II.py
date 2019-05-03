"""Buy at every opportunity and sell at every opportunity. Buy and sell can be made on the same day."""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        total_profit, buy_price = 0, prices[0]

        for p in prices:
        	if p > buy_price:
        		total_profit += p - buy_price
        	buy_price = p

        return total_profit
