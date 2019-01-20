# Explanation

# a) XOR of a number by itself is 0
# b) XOR of a number by 0 is itself

from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce((lambda x, y: x ^ y), nums)

print Solution().singleNumber([1,1,2,2,3,4,4])
