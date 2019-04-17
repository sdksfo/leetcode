"""
Approach:

We sort both arrays in descending order.
Use two pointers to move from left to right for both arrays
If number in i at A is greater than j at B, then we can place the A[i] in the index in unsorted B, where B[j] occurs
Else if that does not happen, we pop the smallest element from A (since technically that has no other position to go) and keep it in jth index.

Complexity:

Time: O(m+n) Space: O(n)
"""


import collections


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        indices = collections.defaultdict(list)

        for i, d in enumerate(B):
        	indices[d].append(i)

        A, B, i, j, output = sorted(A, reverse=True), sorted(B, reverse=True), 0, 0, [0 for _ in A]

        while i < len(A) and j < len(B):
        	if A[i] > B[j]:
        		output[indices[B[j]].pop()] = A[i]
        		i += 1
        	else:
        		output[indices[B[j]].pop()] = A.pop()
        	j += 1

        return output

print Solution().advantageCount([12,24,8,32], [13,25,32,11])
