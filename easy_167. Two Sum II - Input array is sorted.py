
"""Since array is sorted, we can use the two pointer technique"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers)-1

        while i < j:
        	total = numbers[i] + numbers[j]
        	if  total == target:
        		return [i+1, j+1]
        	elif total < target:
        		i += 1
        	else:
        		j -= 1

print Solution().twoSum([2,7,11,15], 22)
