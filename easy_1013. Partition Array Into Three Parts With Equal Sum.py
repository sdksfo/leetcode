"""
Requirement:

Partition array into three parts

Approach:

1) Keep a running total
2) When total reaches expected, increment count and reset total
3) Check if count is 3 at end of iteration

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        expected, total, count = sum(A)/3, 0, 0

        for i in A:
        	total += i
        	if total == expected:
        		count += 1
        		total = 0

        return count == 3
