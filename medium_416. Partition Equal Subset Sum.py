
# backtracking solution

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, s):
        	if s in nums:
        		return True
        	if sum(nums) > s:
	        	for i in xrange(len(nums)):
	        		if dfs(nums[:i]+nums[i+1:], s-nums[i]):
	        			return True
        	return False

    	return dfs(nums, sum(nums)/2) if not sum(nums)%2 else False


# Dynamic Programming Solution

# [1, 5, 5, 11]

# 1  (1,0) (0,1)
# 5. (6,0) (1,5) (5,1) (0,6)
# 5  (17,0) (6,5) (6,5) (1,6) (10,1) (5,6) (5,6) (0,11)

# Each element can be either added to the first or to the second. Iterate until there is an even number on both on adding the last number
# Ignore those bags, whose sum goes over half

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2: return False

        half_sum = sum(nums)/2

        dp = [(0,0)]

        for num in sorted(nums):
        	temp = set()
        	for pair in dp:
        		bag1, bag2 = pair
        		temp.add((num+bag1,bag2)) if num+bag1 <= half_sum else None
        		temp.add((bag1, bag2+num)) if num+bag2 <= half_sum else None
        	dp = list(temp)
        return any([i==j for i,j in dp])

print Solution().canPartition([35,69,8,10,56,85,20,67,39,15,57,19,80,45,12,81,92,98,25,26,51,3,31,16,30,37,55,52,61,17,30,82,52,85,84,83,98,29,79,29,99,70,97,20,42,22,44,44,65,75,70,86,97,100,45,69,91,53,88,96,65,88,92,73,16,57,34,11,64,3,92,48,98,29,39,16,47,92,22,19,50,86,78,68,52,51,70,80,2,58,79,70,91,94,23,47,81,4,18,15])
