



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)

        while i < j:
        	mid = (i + j)/2

        	if nums[mid-1] < nums[mid] > nums[(mid+1)%len(nums)]:
        		return mid
        	elif nums[mid-1] < nums[mid] < nums[(mid+1)%len(nums)]:
        		i = mid + 1
        	else:
        		j = mid

        return i

print Solution().findPeakElement([0,1,2,3,4,2])