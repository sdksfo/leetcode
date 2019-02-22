

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashtable = set()
        for num in nums:
        	if num in hashtable:
        		return True
        	hashtable.add(num)
        return False

print Solution().containsDuplicate([])
