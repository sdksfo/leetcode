
# Based on https://leetcode.com/problems/online-election/discuss/191898/Anybody-has-a-magic-general-formula-for-Binary-Search

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return 0

        i, j = 1, (x/2)+1

        while i < j-1:
            mid = (i + j)/2
            if (mid*mid) <= x:
                i = mid
            else:
                j = mid

        return i

# Short circuits immediately

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i, j = 0, (x/2)+1

        while i < j:
            mid = (i + j)/2

            if (mid*mid) <= x < (mid+1)*(mid+1):
                return mid
            elif (mid*mid) < x:
                i = mid + 1
            else:
                j = mid

        return i
