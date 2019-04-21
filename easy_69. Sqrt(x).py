

# My solution - short circuits immediately

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

# Tristan's solution - exits when i and j cross over


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return 0

        i, j, best = 0, (x/2)+1, 1

        while i <= j:
            mid = (i + j)/2
            if (mid*mid) <= x:
                best = mid
                i = mid + 1
            else:
                j = mid - 1

        return best

