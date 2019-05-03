
"""
Sort based on the difference between costs[0] and costs[1] and assign the first half to A and second half to B
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = sorted(costs, key=lambda i: i[0]-i[1])

        return sum(i[0] for i in m[:len(costs)/2]) + sum(i[1] for i in m[len(costs)/2:])

print Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
