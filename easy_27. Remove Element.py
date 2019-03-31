

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = j = len(nums)-1

        while i >= 0:
        	if nums[i] == val:
        		nums[i], nums[j] = nums[j], nums[i]
        		j -= 1
        	i -= 1
        return j+1

print Solution().removeElement([1], 1)
