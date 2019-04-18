"""
Approach:

Maintain two pointers for even index and odd index and swap, when the element are out of place, swap and increment the indices.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_idx, even_idx, i = 1, 0, 0

        while i < len(A):
        	if not A[i] % 2 and i % 2:
        		A[even_idx], A[i] = A[i], A[even_idx]
        		even_idx += 2
        	elif A[i] % 2 and not i%2:
        		A[odd_idx], A[i] = A[i], A[odd_idx]
        		odd_idx += 2
        	else:
        		i += 1
        return A
