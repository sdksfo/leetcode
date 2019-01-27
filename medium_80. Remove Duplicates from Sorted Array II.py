
# Explanation

# 1, 1, 1, 2, 2, 3, 3, 3

# 1, 1, 2, 2, 1, 2, 3, 3
#             d
#     1) If number changes and there is dup index swap and increment dup index. set counter = 1
# 	  2) If number remains the same and counter is less than 2 swap and increment dup index. set counter + 1

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        counter, dup, prev = 1, 1, nums[0]

        for i in xrange(1, len(nums)):
        	if nums[i] == prev and counter < 2:
        		nums[dup] = nums[i]
        		dup += 1
        		counter += 1
        	elif nums[i] != prev:
        		counter = 1
        		nums[dup] = nums[i]
        		dup += 1
        	prev = nums[i]

        return dup

print Solution().removeDuplicates([0,0,0,0,1])
