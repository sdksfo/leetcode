

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashset, pairs = set(), set()

        for num in sorted(nums):
        	if num - k in hashset:
        		pairs.add((num-k, num))
        	hashset.add(num)

        return len(pairs)

print Solution().findPairs([3, 1, 4, 1, 5,2,3,9,23,329,0], 2)
