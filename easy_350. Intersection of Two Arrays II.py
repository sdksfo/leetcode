

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2, i, j, output = sorted(nums1), sorted(nums2), 0, 0, []

        while i < len(nums1) and j < len(nums2):
        	if nums1[i] == nums2[j]:
        		output.append(nums1[i])
        		i += 1
        		j += 1
        	elif nums1[i] < nums2[j]:
        		i += 1
        	else:
        		j += 1

        return output

print Solution().intersect([1,2,2,1], [2,3,4,4])