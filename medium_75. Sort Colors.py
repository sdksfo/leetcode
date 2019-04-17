"""
Requirement:

a) Given an array of 0,1 and 2, modify to make 0s followed by 1s and 2s.

Approach:

a) Keep two pointers 0ptr and 2ptr at indices 0 and len(array)-1 respectively.
b) Use a third pointer 'i' to iterate through the array.
c) If 0 is encountered during traversal, swap it with the 0ptr and increment the 0ptr and i.
d) If 2 is encountered during traversal, swap with 2ptr and decrement 2ptr.
e) If 1 is encountered, increment i.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero, two, i = 0, len(nums)-1, 0

        while i <= two:
        	if nums[i] == 0:
        		nums[i], nums[zero] = nums[zero], nums[i]
        		zero += 1
        		i += 1
        	elif nums[i] == 1:
        		i += 1
        	else:
        		nums[i], nums[two] = nums[two], nums[i]
        		two -= 1
        return nums

print Solution().sortColors([0,1,2,0,1,2,0])

"""
Requirement:

a) Given an array of 0,1 and 2, modify to make 0s followed by 1s and 2s.

Approach:

a) Iteration 1: Traverse from left to right and move all 0's to the left
b) Iteration 2: Traverse from right to left and move all 2's to the right

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = zero = 0

        while i < len(nums):
        	if nums[i] == 0:
        		nums[i], nums[zero] = nums[zero], nums[i]
        		zero += 1
        	i += 1

        i = two = len(nums)-1

        while i >= 0 and nums[i]: # reverse traversal helps to not traverse through the 0s at the front
        	if nums[i] == 2:
        		nums[i], nums[two] = nums[two], nums[i]
        		two -= 1
        	i -= 1

        return nums

print Solution().sortColors([0,1,2,0,1,2,0,2,0,1,1,2,0,2])
