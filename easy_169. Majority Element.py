

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, ctr = nums[0], 0

        for num in nums:
        	if num == majority or ctr == 0:
        		ctr += 1
        		majority = num
        	else:
        		ctr -= 1
       	return majority

print Solution().majorityElement([1,1,2,3,1])
