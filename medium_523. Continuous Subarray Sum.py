
# Observation:

# # O(n2) solution is to check if anything from 0 to n sums to multiples of k

# Is there a better solution

# What is the total sum of the array and what is the possible multiple within the total sum

# Once we have this, all we have to do is find if there is a pair or more, that matches this condition

# [23, 2, 4, 6, 7]

# 23, 25, 29, 35, 42

# 6, 12, 18, 24, 30, 36, 42


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums: return False
        cache, total = {}, 0
        for i,v in enumerate(nums):
            total += v
            m = total % k
            if (m == 0 and i > 0) or i-cache.get(m,i) > 1: return True
            if m not in cache: cache[m] = i
        return False

print Solution().checkSubarraySum([23,2,6,4,5], 6)
