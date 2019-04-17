"""
Requirement:

Generate a pascal's triangle

Approach:

a) Iterate from 1 thru numRows
b) For building the pascal's triangle value for each row, apply the below logic:
	a) Iterate 'i' from 0 to row-1 ie if row is 2, iterate from 0 through 1
	b) If 'i' is 0 or row-1, value in the pascal triangle is '1'
	c) If 'i' is not 0 or row-1, value in the pascal triangle is prev_row[i-1] + prev_row[i]

Complexity:

Time: O(n) Space: O(n)
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for row in xrange(1, numRows+1):
        	output.append([1 if i == 0 or i == row-1 else output[-1][i-1] + output[-1][i] for i in xrange(row)])
        return output

print Solution().generate(0)
