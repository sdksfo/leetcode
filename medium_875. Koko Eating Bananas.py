"""
The monkey can eat anywhere from 1 to the size of the biggest pile.

For each number from 1 to largest size, try to run a binary search and find how many hrs it takes. If time taken < H, then monkey
is eating faster than it should, hence decrease the speed, else otherwise increase the speed. The lowest required speed to
eat all bananas within the alloted time is the answer. Spent 2 hrs on this problem.

Complexity (plogM), where p is the size of the piles, and  1 <= M <= max_pile_size
"""

class Solution(object):
    def computeHrs(self, piles, speed, hrs=0):
        for pile in piles:
            hrs += (pile/speed) + (pile%speed != 0)
        return hrs

    def minEatingSpeed(self, piles, H):
        i, j = 1, max(piles)

        while i <= j:
            speed = (i + j)/2
            time_taken_to_eat = self.computeHrs(piles, speed)
            if time_taken_to_eat <= H:
                j = speed - 1
            else:
                i = speed + 1
        return i
