"""
Requirement:

Calculate fibonnacci

Approach:

Use two variables and do a sliding window

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 or N == 1:
        	return N

        first, second = 0, 1

        for i in range(2, N+1):
        	first, second = second, second + first

        return second

print Solution().fib(6)
