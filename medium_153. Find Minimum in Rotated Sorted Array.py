
class Solution(object):
    def findMin(self, nums):
        i, j = 0, len(nums)-1

        while i < j:
            mid = (i+j)/2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1
        return nums[i]
