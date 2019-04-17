"""
Requirement:

Given an array of non-negative integers, determine if you are able to reach the last index.

Approach:

1) Start from the first index and check how far we could go. Keep it as max_distance.
2) In each point along the way from start index to max_distance, check if we could reach beyond the max_distance.
3) If we could reach a distance farther than the distance computed in step 1), adjust the max_distance pointer accordingly. Rinse and repeat step 2) and 3)
4) Return True if 2) and 3) takes to end of array else False

Complexity:

Time: O(n) Space: O(1)
"""


class Solution(object):
    def canJump(self, nums):
        max_distance = 0
        for i in xrange(len(nums)):
            if i > max_distance: return False
            max_distance = max(max_distance, i+nums[i])
        return True

print Solution().canJump([0])
