"""
Requirement:

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Approach:
a) The array could have negative numbers, whose squares then could throw off the sorted order if sent as they come.
b) Use two pointers to surf left and right of the input array.
c) If the abs of left is less than abs of right, insert pow(right, 2) in right of output. Decrement the jth pointer.
d) Else insert pow(left, 2) in right of output and increment the ith pointer.

Complexity:

Time: O(n) space: O(1)
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j , output, ptr = 0, len(A) - 1, A[:], len(A) - 1

        while i <= j:
            if abs(A[i]) < abs(A[j]):
                output[ptr] = A[j] * A[j]
                j -= 1
            else:
                output[ptr] = A[i] * A[i]
                i += 1
            ptr -= 1
        return output

print Solution().sortedSquares([])
