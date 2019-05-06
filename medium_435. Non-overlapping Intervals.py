
# Approach: Sort by increasing order of ending times (to keep the ones ending first and discard rest).
# If the start time of an interval is less than the end time of previous interval, then its overlapping and remove it.
# Similar to bursting ballons or merging intervals problem.

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals, removed = sorted(intervals, key=lambda x: x[1]), 0

        prev_end = float('inf')

        for interval in intervals:
        	start, end = interval
        	if start < prev_end:
        		removed += 1
        	else:
        		prev_end = end

        return removed
