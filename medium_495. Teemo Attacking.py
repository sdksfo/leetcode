"""
Requirement:

Check how long poison lasts

Approach:

Poison lasts only as much as the difference between the min(next time slice - curr time slice, duration)

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poison_state = 0

        for i in range(len(timeSeries)-1):
        	poison_state += min(timeSeries[i+1]-timeSeries[i], duration)

        return poison_state + duration if timeSeries else 0
