

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max, curr_min, total_max = nums[0], nums[0], nums[0]

        for i in xrange(1, len(nums)):
            curr_max, curr_min = max(curr_max*nums[i], curr_min*nums[i], nums[i]), min(curr_max*nums[i], curr_min*nums[i], nums[i])
            total_max = max(curr_max, total_max)
        return total_max

print Solution().maxProduct([-4,-3,-2])
