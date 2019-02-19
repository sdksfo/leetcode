


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
       	for num in nums:
       		n ^= num
       	return n

print Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])