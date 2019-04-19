

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def compute(x, n):
        	if n == 0:
        		return float(1)

        	partial = compute(x, float(n)/2)

        	if n%2:
        		return x * partial * partial
        	else:
        		return partial * partial

        return 1/compute(x, abs(n)) if n < 0 else compute(x, n)