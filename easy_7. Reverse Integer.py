

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num, total = abs(x), 0

        while num:
        	total = (total*10) + (num%10)
        	num = num/10

        return 0 if total > (2**31)-1 else (total if x > 0 else -total)

print Solution().reverse(1534236469)
