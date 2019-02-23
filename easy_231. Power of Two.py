
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n:
            return (n) & (n - 1) == 0
        return False
