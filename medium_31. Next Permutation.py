
# Explanation

# Going over a few examples to derive a pattern

# a) All increasing sequence

# 1,2,3,4 -> swap the last two -> 1,2,4,3

# b) All decreasing sequence

# 4,3,2,1 -> return the sorted

# c) Non-monotonous sequence

# Scan the array to find the last peak ie where the array goes down from increasing to decreasing order

# ie in e.g [1,2,3,1,2,5,3,1,0], the last peak is element 5 after which the array is decreasing

# So the case can be simplified as increasing until 5 and decreasing thereafter.

# Using e.g a) and b) above, we can write the rules as

# i) Apply swapping rule for until 5 (Increasing sequence)

# There is a small trick here though, in increasing sequence e.g 1,2,3,9 we swapped 3 and 9 to get next perm, since 9 is the next highest number for 3.
# So likewise we find what is the next highest number for '2' (idx 4) [1,2,3,1,2,5,3,1,0]. So that instead of swapping 2(idx 4) and 5 (idx 5), we should swap 2 with the next highest number
# which is 3.

# So applying this rule, the array will become [1,2,3,1,3,5,2,1,0]

# ii) Apply sorting for elements after 5 (Decreasing sequence)

# So the array becomes: [1,2,3,1,3,5,0,1,2], which is the next permutation for [1,2,3,1,2,5,3,1,0].

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
        	return nums
        last_peak = None
        for i in xrange(1, len(nums)):
        	if nums[i] > nums[i-1]:
        		last_peak = i - 1

        if last_peak is not None:
        	min_idx = last_peak + 1
        	for i in xrange(last_peak+1, len(nums)):
        		if nums[min_idx] > nums[i] > nums[last_peak]:
        			min_idx = i
        	nums[min_idx], nums[last_peak] = nums[last_peak], nums[min_idx]
        	nums[:] = nums[:last_peak+1]+sorted(nums[last_peak+1:])
        else:
        	nums[:] = nums[::-1]

print Solution().nextPermutation([2,3,1,3,3])
