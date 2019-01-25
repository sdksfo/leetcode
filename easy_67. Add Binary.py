
# Explanation

# For binary addition: 1+0 = 1, 0+0 = 1, 1+1 = 0 with a carry of 1, 1+1+1 = 1 with a carry of 1. Count the
# number of 1's to determine the output and the carry

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c, output = '0', ''
        b = '0' * (len(a)-len(b)) + b if len(a) > len(b) else b
        a = '0' * (len(b)-len(a)) + a if len(b) > len(a) else a

        for i in xrange(len(a)-1,-1,-1):
            count = (a[i]+b[i]+c).count('1')
            sum_ = '1' if count%2 else '0'
            c = '0' if count < 2 else '1'
            output = sum_ + output

        return c + output if c == '1' else output

print Solution().addBinary('11', '11')
