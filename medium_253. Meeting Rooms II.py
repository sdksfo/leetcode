
"""
Use a min-heap to store the meeting completion times. When a new meeting is started,
we look at the min-heap to decide if any existing room will be available and can be re-used or if a new meeting room be
allocated.
"""

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals, ralloc = sorted(intervals, key=lambda x: x.start), []
        for i in intervals:
        	if ralloc:
        		prev_meeting_room = heapq.heappop(ralloc)
        		if i.start >= prev_meeting_room[0]: # old room can be re-used
        			heapq.heappush(ralloc, (i.end, prev_meeting_room[1]))
        		else:
        			heapq.heappush(ralloc, prev_meeting_room)
        			heapq.heappush(ralloc, (i.end, i.start)) # new meeting room to be allocated
        	else:
        		heapq.heappush(ralloc, (i.end, i.start))
        	heapq.heapify(ralloc)
        return len(ralloc)

t = [Interval(*i) for i in [[9,10],[4,9],[4,17]]]

print Solution().minMeetingRooms(t)
