"""
Approach:

Take into account the below edge case:

[2,2,2,2,2] => 2 * 5
[5,5] => 5 * 2

h_idx is the minimum for both the cases ie 2

ln: hval = min(c, cl-i), does that computation

Time: O(nlogn)
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        cs, hidx, cl = sorted(citations), 0, len(citations)

        for i, c in enumerate(cs):
        	hval = min(c, cl-i)
        	hidx = max(hidx, hval)

        return hidx

print Solution().hIndex([100, 200, 300, 500, 1000])
