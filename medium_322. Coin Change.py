
"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


Solution:

Solved with DP. For amount 11, and coins [1,2,5], recurrence is written as:
dp[11] = min(change using 1$, change using 2$, change using 5$) or in other words
dp[11] = min(1 + dp[10], 1 + dp[9], 1 + dp[6])
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for i in xrange(amount+1)]

        for i in xrange(1, amount+1):
        	dp[i] = min([1 + dp[i-j] for j in coins if (i-j) >= 0] or [float('inf')])

        return -1 if dp[-1] == float('inf') else dp[-1]


print Solution().coinChange([1,2,5], 11)
