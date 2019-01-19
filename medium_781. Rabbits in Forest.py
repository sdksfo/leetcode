
# Explanation:

# Going over with an example is easier to understand this problem. For simplicity sort the rabbits like below:

# a) [2,2,2,2,2] = 2,2,2 | 2,2 => 3 + 3 = 6 rabbits
# b) [2,2,2,3,3,3,3,3] = 2,2,2 | 3,3,3,3 | 3 = 3 + 4 + 4 = 11 rabbits

# In e.g (a) The first 3 rabbits could be from same color, The second group could be from same color group
# In e.g (b) The first 3 rabbits are same color, The second group of 4 rabbits are same color and the last rabbit is a different color

# So mathematically, its applying division and modulo for grouping and counting

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        seen = set()
        min_rabbits = 0

        for rabbit in answers:
        	if rabbit not in seen:
        		seen.add(rabbit)
        		rabbits = answers.count(rabbit)
        		min_rabbits += (rabbits/(rabbit+1)) * (rabbit+1)
        		min_rabbits += (rabbit+1) if rabbits % (rabbit+1) else 0

        return min_rabbits

print Solution().numRabbits([10, 10, 10])
