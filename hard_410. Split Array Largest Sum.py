"""
Pick a number from num_max to num_sum and check using binary search whats the least number that can split 'm' ways.
"""

class Solution(object):
    def numSplits(self, nums, expected):
        total, splits = 0, 0
        for num in nums:
            total += num
            if total > expected:
                total = num
                splits += 1
            if total == expected:
                splits += 1
                total = 0
        return splits + 1 if total else splits

    def splitArray(self, nums, m):
        i, j = max(nums), sum(nums)

        while i < j:
            mid = i + (j-i)/2
            if self.numSplits(nums, mid) <= m:
                j = mid
            else:
                i = mid + 1

        return i
