
# Explanation
# Keep track of permutations at each level and only add to solution if its not already added.

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums]
        solution = set()
        for perm in self.permuteUnique(nums[1:]):
            for char in xrange(len(perm)+1):
                permute = perm[:char]+[nums[0]]+perm[char:]
                solution.add(tuple(permute))
        return [list(i) for i in solution]

print Solution().permuteUnique([1,1,3,4])
