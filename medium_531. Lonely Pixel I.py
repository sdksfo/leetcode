"""
a) Iterate once and store a hashmap of row-val and col-val and the counts of 'B' in each row or col
b) Iterate again and check for each black pixel, if its corresponding row and col values in the hashmap has count of 1

Time: O(m*n) Space: O(m+n)
"""

import itertools

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture: return 0

        rows, cols, row, col, ctr =  len(picture), len(picture[0]), collections.defaultdict(int), collections.defaultdict(int), 0

        for r, c in itertools.product(range(rows), range(cols)):
            if picture[r][c] == 'B':
                row[r] += 1
                col[c] += 1

        for r, c in itertools.product(row.keys(), col.keys()):
            if picture[r][c] == 'B' and row[r] == col[c] == 1:
                ctr += 1
