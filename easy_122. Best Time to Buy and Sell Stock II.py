
# Explanation:

# Profit is maximal if the user buys every day and sells at every selling opportunity

# Only three series are mathematically possible:

# a) monotonic decreasing e.g [6, 5, 4]
    # profit is 0 as no sale is possible

# b) monotonic increasing
    # e.g [1, 5, 20, 200]

    # by induction its buy at 1 and sell at 200 for max profit ie 200 - 1 = 199

    # And mathematically its the same as (5-1) + (20-5) + (200-20) or the below transactions in order:

    #     a) buy for 1 and sell for 5
    #     b) buy for 5 and sell for 20
    #     c) buy for 20 and sell for 200

# c) bitonic sequence:

# for both (first decrease and then increase) or (first increase and then decrease), just buy every day and sell when there is an opportunity

# e.g) Consider the series, [1, 2, 17, 5, 20, 200]

# Inspecting the data, its obvious that buy for 1$ and sell for 17$. Buy again for 5$ and sell for 200$ would give a total profit of 211$

# But lets see, how much he will make if he buys every day and sells at any day when the price goes up

# day 1: Buy for 1$. No sale done
# day 2: Sell for 2$. profit = 2 - 1= 1. The user also buys for 2
# day 3: Sell for 17. profit = 17 - 2 = 15. The user buys for 17
# day 4: No sale done as price drops from 17 to 5. User buys for 5
# day 5: Sells for 20. profit = 20 - 5 = 15. User buys for 20
# day 6: Sells for 200. profit = 200 - 20 = 180

# Total cumulative profit = 1 + 15 + 15 + 180 = 211$.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, buying_price = 0, prices[0] if prices else 0

        for i in xrange(len(prices)):
            if prices[i] > buying_price:
                profit += prices[i] - buying_price
            buying_price = prices[i]

        return profit

print Solution().maxProfit([])
