"""

Things to note here:

a) why is 'j' assigned mid instead of mid - 1  ===> since nums[mid] < nums[j], mid could be the smallest in the array technically. So we include
mid in our next iteration
b) Why is return nums[j] instead of nums[i] ===> Typically in binary search, i moves from left to right and j from right to left.
But here, only i is moving and j is not moving. So if we start 'i' at 0 and 'j' at 5, 'i' ptr is the only one moving and hence
it would move beyond 'j' for the loop to terminate. Hence we return 'j' instead of 'i'.

"""

class Solution(object):
    def findMin(self, nums):
    	i, j = 0, len(nums)-1

        while i <= j:
            mid = (i+j)/2
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1

        return nums[j]
