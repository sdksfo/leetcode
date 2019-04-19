"""
a) For each house, check what is the closest heater ie on its left or its right
b) The minimum radius is the maximum of the minimum distances for all the houses(computed using above).

Complexity: O(nlogn + mlogn), where m are 'houses' and 'heaters'
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        heaters, max_luminence = [-float('inf')] + sorted(heaters) + [float('inf')], 0

        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            closest_light = min(heaters[idx]-house, house-heaters[idx-1])
            max_luminence = max(closest_light, max_luminence)

        return max_luminence

print Solution().findRadius([1,5], [2])
