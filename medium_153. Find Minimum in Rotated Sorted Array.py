
"""
Idea:

Using binary search, three scenarios are possible:

a) min is on the left side of array
b) min is on the right side of array
c) min is at the pivot or mid

Since, the array is rotated, if we deduce the base condition for searching in left side ie min on left side, we can use 'else' clause to direct search on right side for other cases.

Only the below sequences are possible for min to lie on the left side:

a) 7,8,9,0,1,2,3,4,5
b) 0,1,2,3,4,5,6,7,8

For both these, the condition can be written as

(nums[mid] <= nums[j] and nums[mid] <= nums[i]) or (nums[mid] <= nums[j] and nums[mid] >= nums[i]), where mid is pivot or middle of the array

"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search(i, j, k):
            mid = (i+j)/2
            if nums[mid] <= nums[mid-1] and nums[mid] <= nums[(mid+1)%k]: #used modulo to avoid bound errors
                return nums[mid]
            elif (nums[mid] <= nums[j] and nums[mid] <= nums[i]) or (nums[mid] <= nums[j] and nums[mid] >= nums[i]):
                return search(i, mid-1, k) #123456
            else:
                return search(mid+1, j, k)
        return search(0, len(nums)-1, len(nums))

print Solution().findMin([6,7,8,9,10,11,1])
