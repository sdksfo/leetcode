
# Explanation

# We keep a track for what is the maximum distance we can cover from a certain index. Once we reach the maximum
# reachable distance, we try to again jump and see if we can maximise further.

# Note: Referred this solution from EPI, chapter 2: Array

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable, last_index, i = 0, len(nums) - 1, 0

        while i <= max_reachable and max_reachable < last_index:
            max_reachable = max(max_reachable, nums[i]+i)
            i += 1

        return max_reachable >= last_index

print Solution().canJump([5])
