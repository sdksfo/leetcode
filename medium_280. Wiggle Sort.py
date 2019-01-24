
# Explanation

# Take sorted input and fill the alternate indexes with next higher number

# Sorting and re-ordering

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        i, j = 1, len(nums) - 1

        while i < j:
            nums.insert(i, nums.pop())
            i += 2

# For even indices, compare and swap if odd indices are lesser than even
# For odd indices, compare and swap if even indices are greater than odd

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-1):
            if not i%2 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i%2 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

print Solution().wiggleSort([3,5,2,1,4])
