
from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap1, hashmap2, output = defaultdict(int), defaultdict(int), []
        for i in nums1:
            hashmap1[i] += 1
        for i in nums2:
            hashmap2[i] += 1
        for num in hashmap1:
            if num in hashmap2:
                output.extend([num]*min(hashmap1[num], hashmap2[num]))

        return output

print Solution().intersect([4,9,5], [9,4,9,8,4])
