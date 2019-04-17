"""
Requirement:

Count and say the sequence of integers.

Approach:

1) char comparison

Complexity:

Time: O(n*m), where m is the max length of string
Space: O(1)
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        output = '1'

        for i in xrange(1, n):
            count, prev, temp = 1, output[0], ''
            for i in output[1:]:
                if i != prev:
                    temp += '%s%s' %(count, prev)
                    count = 0
                count, prev = count + 1, i
            temp += '%s%s' %(count, prev)
            output = temp

        return output

print Solution().countAndSay(5)
