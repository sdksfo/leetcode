
# Approach 1: Count the number of 0s 'before' and 'after'. Whenever a new zero is countered, do
# a sum of 'before' and 'after' and reset 'after' as ur new 'before'.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums: return len(nums)

        prev = after = max_count = 0

        for num in nums:
            if num == 0:
                max_count = max(max_count, prev+after+1)
                prev, after = after, 0
            else:
                after += 1

        return max(max_count, prev+after+1)

print Solution().findMaxConsecutiveOnes([1,0,0,0,0,1,1,1,1,1,1,1,1,1,0])
