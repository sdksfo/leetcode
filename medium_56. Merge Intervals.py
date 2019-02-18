# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        stack = [intervals[0]] if intervals else []

        for i in xrange(1, len(intervals)):
            if intervals[i].start <= stack[-1].end:
                old_interval = stack.pop()
                new_interval = Interval(old_interval.start, max(old_interval.end, intervals[i].end))
                stack.append(new_interval)
            else:
                stack.append(intervals[i])
        return stack
