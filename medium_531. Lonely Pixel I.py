
"""Check right and down, marking each B as W if already seen. If lonely pixel add to the counter"""

import itertools

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        rows, cols, pixels = len(picture), len(picture[0]) if picture else 0,  0

        valid_rows = set([idx for idx, row in enumerate(picture) if row.count('B') == 1])
        valid_cols = set([idx for idx, col in enumerate(zip(*picture)) if col.count('B') == 1])

        for row, col in itertools.product(valid_rows, valid_cols):
            pixels += 1 if picture[row][col] == 'B' else 0

        return pixels

print Solution().findLonelyPixel([["W","W","W"],["W","W","0"],["W","W","B"]])
