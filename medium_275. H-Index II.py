"""
Move towards the number which will give the max citations possible
"""

# Approach 1 - where we also makes it obvious the thing that we could find something like [5,6] where 2 is hindex

class Solution(object):
    def hIndex(self, arr):
        """
        :type citations: List[int]
        :rtype: int
        """
        i, j, arr_len, hidx = 0, len(arr), len(arr), 0

        while i < j:
            mid = i + (j-i)/2
            if arr[mid] <= (arr_len-mid):
                hidx = max(hidx, arr[mid])
                i = mid + 1
            else:
                hidx = max(hidx, min(arr[mid], arr_len-mid))
                j = mid

        return hidx


# Approach 2 - Less obvious, but we move the 'i' towards the max index on the right, which is lesser than (arr_len-mid)

class Solution(object):
    def hIndex(self, arr):
        """
        :type citations: List[int]
        :rtype: int
        """
        i, j, arr_len = 0, len(arr), len(arr)

        while i < j:
            mid = i + (j-i)/2
            if arr[mid] < (arr_len-mid):
                i = mid + 1
            else:
                j = mid

        return arr_len - i

print Solution().hIndex([0,1,5,6])
