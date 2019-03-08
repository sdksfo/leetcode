

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def getPow(x, n):
            if n == 0:
                return float(1)

            half_num = getPow(x, n/2)

            if n % 2:
                return half_num * half_num * x
            else:
                return half_num * half_num

        return getPow(x, n) if n > 0 else 1/getPow(x, abs(n))

print Solution().myPow(2.00000, 10)
