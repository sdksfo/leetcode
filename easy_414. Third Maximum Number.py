"""
Approach:

Keep there variables and update them based on the number in the array

Complexity:

Time: O(n) Space: O(1)
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None

        for n in nums:
            if n not in (first, second, third):
                if n > first:
                    first, second, third = n, first, second
                elif n > second:
                    second, third = n, second
                elif n > third:
                    third = n

        return third if third is not None else max(first, second)
