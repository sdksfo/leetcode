
# Explanation

# Maintain a ptr for the first duplicate element and whenever the current element == past element, move that to the first duplicate_index


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        dup_idx, prev_element = None, nums[0]

        for i in xrange(1, len(nums)):
        	if nums[i] == prev_element and not dup_idx:
        		dup_idx = i
        	if nums[i] != prev_element and dup_idx:
        		nums[dup_idx] = nums[i]
        		dup_idx += 1
        	prev_element = nums[i]

        return dup_idx or len(nums)

print Solution().removeDuplicates([1,1,2])
