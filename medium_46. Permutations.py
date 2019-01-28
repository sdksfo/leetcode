
# Explanation

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# Perm of 1 = 1
# Perm of 1,2 = 2 + Perm of 1 = 2 + [1] = [2,1], [1,2]
# Perm of 1,2,3 = 3 + Perm of 1,2 = [3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,2,3], [1,3,2]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        return [perm[:char]+[nums[0]]+perm[char:] for perm in self.permute(nums[1:]) for char in xrange(len(perm)+1)]

print Solution().permute([1,2,3])
