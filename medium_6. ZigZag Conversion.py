
# Explanation

# For n=4, move from 0 -> 3 -> 0. Use a step variable to add or subtract.

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        buckets, bucket, step = ['' for i in xrange(numRows)], 0, 1
        for char in s:
        	buckets[bucket] += char
        	bucket += step
        	step = -step if bucket in (numRows - 1, 0) else step
        return ''.join(buckets)

print Solution().convert('PAYPALISHIRING', 1)
