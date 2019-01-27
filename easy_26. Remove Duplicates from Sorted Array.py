
# Explanation

# Maintain a ptr for the first duplicate element and whenever the current element == past element, move that to the first duplicate_index


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        first_dup = 1

        for i in xrange(1, len(nums)):
        	if nums[i] != nums[first_dup-1]:
        		nums[first_dup] = nums[i]
        		first_dup +=1

        return first_dup

print Solution().removeDuplicates([1,1,2,3,3,4])
