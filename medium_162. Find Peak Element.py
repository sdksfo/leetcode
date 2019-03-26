
# O(n) solution is easy as we need to just traverse the array. Lets implement that first and then probably do the binary search version

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        for i in xrange(len(nums)):
          if i > 0 and i < len(nums)-1:
              if nums[i-1] < nums[i] > nums[i+1]: return i
          elif i == 0:
              if nums[i] > nums[i+1]: return i
          elif i == len(nums) - 1:
              if nums[i] > nums[i-1]: return i

print Solution().findPeakElement([1,2,1,3,5,6,4])

class Solution(object):
    def findPeakElement(self, nums):
        i , j = 0 , len(nums) - 1
        while i < j:
            mid = (i + j)/2
            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid+1
        return i

print Solution().findPeakElement([1,2,1,1,1,1])
