

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = set(nums1), set(nums2)
        return [i for i in nums1 if i in nums2]


print Solution().intersection([1,2,3,7,8,9,2], [4,5,2,3,2])
