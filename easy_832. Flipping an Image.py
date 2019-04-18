"""
Approach:

For flipping numbers, just do 1-i, where 'i' is 1/0

Complexity:

O(n)
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        for row in A:
        	row = [1-i for i in row]
        	output.append(row[::-1])
        return output
