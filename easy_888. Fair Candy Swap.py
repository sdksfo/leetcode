"""
Requirement:

Swap candies to make the count the same

Approach:

Similar to two sum appraoch. But i guess we can use sets to just check if the difference between A and expected is in B.

Complexity:

Time: O(n), Space: O(n)
"""

class Solution(object):
    def get_diff(self, a, b, exp):
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] - b[j] == exp:
                return [a[i], b[j]]
            elif a[i] - b[j] > exp:
                j += 1
            else:
                i += 1

    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B.sort()

        a_sum, b_sum = sum(A), sum(B)

        if a_sum > b_sum:
            return self.get_diff(A, B, (a_sum - b_sum)/2)
        else:
            return self.get_diff(B, A, (b_sum - a_sum)/2)[::-1]

print Solution().fairCandySwap([1,2,5], [2,4])
