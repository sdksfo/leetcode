"""
Requirement:

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

Approach:

Appraoch 1:

Iterate forward and also once backward. Check whats the distance between the seats on either direction

Approach 2:

Check groups of 0s. The middle seat in the group is the farthest from the 1. Only condition to check
for is the empty seat on the left and empty seat on the right as these are already farthest from the 1.

Complexity:

Time: O(n) Space: O(n) (if approach 1 else O(1))
"""

# Approach 1: Iterating on sitting on left and sitting on right to determine maximum distance


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        nearest_person, output, maxi = float('INF'), [0 for _ in seats], 0

        for location in xrange(len(seats)):
            seat = seats[location]
            if seat == 0:
                output[location] = location-nearest_person
            else:
                nearest_person = location

        nearest_person = float('INF')

        for location in xrange(len(seats)-1, -1, -1):
            seat = seats[location]
            if seat == 0:
                maxi = max(maxi, min(nearest_person-location, output[location]))
            else:
                nearest_person = location

        return maxi

# Approach 2: Determine the maximum length of 0s to determine the farthest seat

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxi = lseat = count = 0

        rseat = len(seats) - 1

        while lseat < len(seats):
            if seats[lseat]: break
            lseat += 1

        while rseat > -1:
            if seats[rseat]: break
            rseat -= 1

        for seat in seats[lseat:rseat]:
            if not seat:
                count += 1
            else:
                count = 0
            maxi = max(maxi, count)

        return max(((maxi+1)/2 if maxi % 2 else (maxi/2)), len(seats)-1-rseat, lseat)
