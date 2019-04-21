"""
For a range of weights from max(weight) to total(weights), we determine how many days it will take to ship.
Depending on which direction it sways, we either increase the capacity of the ship or decrease it.
"""
class Solution(object):
    def canShip(self, weights, limit):
        cargo, i, days = 0, 0, 1
        for w in weights:
            if cargo + w > limit:
                days += 1
                cargo = 0
            cargo += w
        return days

    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        i, j = max(weights), sum(weights)
        while i < j:
            mid = (i + j)/2
            if self.canShip(weights, mid) <= D:
                j = mid
            else:
                i = mid + 1
        return i

print Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10,20,29,10,12,2,1], 5)
