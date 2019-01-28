
# Explanation

# Do a forward scan and maintain a hashtable of whats the maximum we can earn on that index by selling
# Do a reverse scan and decide whats the maxium we can earn by buying on that index. Refer the hashtable to decide the total_profit
# profit that can be earned if the second buy is made at that point


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy, sell, max_profit, total_profit = prices[0], prices[-1], 0, 0

        hashtable = [0]

        for i in xrange(1, len(prices)):
            max_profit = max(prices[i] - buy, max_profit)
            buy = min(prices[i], buy)
            hashtable.append(max_profit)

        max_profit = 0

        for i in xrange(len(prices)-1, -1, -1):
            max_profit = max(sell-prices[i], max_profit)
            sell = max(prices[i], sell)
            total_profit = max(max_profit+hashtable[i], total_profit)

        return total_profit

print Solution().maxProfit([3,3,5,0,0,3,1,4])
