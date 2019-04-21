

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i, j = 0, len(A)

        while i < j:
            mid = (i+j)/2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            if A[mid] < A[mid+1]:
                i = mid + 1
            else:
                j = mid

print Solution().peakIndexInMountainArray([0,1,2,3,4,5,6,7,8,9,3,2,2,1,1,0])
