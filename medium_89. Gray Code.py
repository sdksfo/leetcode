
"""
Going over a few examples to describe my idea:

Input: 1

output = [0, 1]

Input: 2

Build using the result from input=1 by adding 0s and 1s to every element from prev result which is [0, 1]

a) For 0 (first element from input=1)

Adding '0' and '1' to '0', would make it ['00', '01']

b) For 1 (second element from input=1)

Now we would want to add '1' and '0' to '1' instead of '0' and '1'. Here is the reasoning:

Between 0 and 1 from input=1, there is exactly one bit differing between successive elements. And as
part of building results for 2, the most recent bit that we added was '1'. So adding '0' to the current
bit would make the current element differing by two bits. So we add '1' instead to keep the difference as 1 bit.

Summary:

input => 1 = [0, 1]
input => 2 = [00, 01] (adding '0' & '1' to first element in input 1) + [11, 10] (adding '1' & '0' to second element in input 1) == [0, 1, 3, 2]

Input: 3

Do the same ie add '0'&'1' to elements in even indices and adding '1'&'0' to elements in odd indices from previous result
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def get_bin(n):
            if n < 2:
                return ['0', '1'][:n+1]
            prev, output = get_bin(n-1), []
            for i in xrange(len(prev)):
                output.extend([prev[i]+'0', prev[i]+'1']) if not i%2 else output.extend([prev[i]+'1', prev[i]+'0'])
            return output
        return [int(i, 2) for i in get_bin(n)]

print Solution().grayCode(3)
