
"""
a) Create an array of the cars (from closest to destination to the farthest)
b) Compute the time taken to reach destination. speed = distance/time ie time = distance/speed
c) Using we have time taken to reach the destination for cars sorted by their positions wrto the destination, we can determine
   if the cars coming behind can catch up with the car at the front.
"""


class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = []

        for p, s in sorted(zip(position, speed), reverse=True):
        	times.append((target-p)/float(s))

        fleets, prev = 0, 0

        for i in xrange(len(times)):
        	if times[i] > prev:
        		fleets += 1
        		prev = times[i]

        return fleets

print Solution().carFleet(10, [0,4,2], [2,1,3])
