"""
Binary search and call the guess API with the mid of the range.

Time: O(logn)
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n

        while True:
            choice = (i + j) / 2
            ans = guess(choice)
            if ans == 0:
                return mid
            elif ans < 0:
                j = mid - 1
            else:
                i = mid + 1
