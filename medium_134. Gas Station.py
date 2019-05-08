
# Approach1: Passes LC: Find the gas station to start, from where the fuel never drops < 0 and then check
# if you can traverse the whole stations doing that.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start_idx, fuel = None, 0

        for i in xrange(len(gas)):
        	fuel += gas[i] - cost[i]
        	if start_idx is None and fuel > 0:
        		start_idx = i
        	elif fuel < 0:
        		fuel, start_idx = 0, None

        fuel = 0

        for i in xrange(start_idx, len(gas)+start_idx):
        	i = i%len(gas)
        	fuel += gas[i] + cost[i]
        	if fuel < 0: return -1

        return start_idx

print Solution().canCompleteCircuit([1,4,2,3,1,20], [3,1,1,2,1,1])
