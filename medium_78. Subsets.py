
"""

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
        	prev = self.subsets(nums[1:])
        	return prev + [[nums[0]] + i for i in prev]
        return [[]]

print Solution().subsets([1, 2, 3])