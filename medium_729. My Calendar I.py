"""
Idea: Create a sorted array of start times. For every new booking use binary search
to determine the insert position. At the time of insertion, return if its double booking
under the below scenarios:

a) There is already one event with the same start time (or)
b) The previous meeting ends after the current booking
"""
import bisect

class Event:
    def __init__(self,start, end):
        self.start = start
        self.end = end

    def has_intersect(self, other):
        if other.end <= self.start or self.end <= other.start:
            return False
        return True

    def __lt__(self, other):
        return self.start < other.start

class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start, end) :
        cur_event = Event(start,end)
        if self.events:
            idx = bisect.bisect_left(self.events, cur_event)
            if idx > 0 and cur_event.has_intersect(self.events[idx-1]):
                return False
            if idx < len(self.events) and cur_event.has_intersect(self.events[idx]):
                return False
        else:
            idx = 0
        self.events.insert(idx, cur_event)
        return True

# Your MyCalendar object will be instantiated and called as such:

obj = MyCalendar()
for t in [[37,50],[33,50]]:
    print obj.book(*t)
