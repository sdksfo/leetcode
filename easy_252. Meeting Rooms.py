
"""
If the start time of each meeting is after the end time of previous
meeting he can attend the meeting
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=(lambda x: x.start))
        prev = None

        for i in xrange(len(intervals)):
        	if prev and intervals[i].start < prev.end:
        		return False
        	prev = intervals[i]
        return True

print Solution().canAttendMeetings([Interval(5, 10), Interval(9, 20)])
