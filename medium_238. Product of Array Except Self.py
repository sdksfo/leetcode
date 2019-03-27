
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums:
        	output = [1]
        	for i in xrange(1, len(nums)):
        		output.append(nums[i-1]*output[-1])
        	prod_after = 1
        	for i in xrange(len(output)-2, -1, -1):
        		prod_after *= nums[i+1]
        		output[i] *= prod_after
        	return output

print Solution().productExceptSelf([1,2,0,4])
