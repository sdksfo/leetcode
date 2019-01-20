
# Explanation

# For each house the cost of painting the house ie cost of red house = min(prev_blue+red, prev_green+blue)
# minimal_cost of painting = min(r_cost, b_cost, g_cost)

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        pr, pg, pb = 0, 0, 0
        for cost in costs:
        	r, g, b = cost
        	pr, pg, pb = min(r+pg, r+pb), min(g+pr, g+pb), min(b+pr, b+pg)
        return min(pr, pg, pb)

print Solution().minCost([[17,2,17],[16,16,5],[0,3,19]])
