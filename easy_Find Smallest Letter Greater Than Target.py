"""
Approach:

Regular binary search without any change.

Note: The final return statement is to process any element that lies to the left of first index or the right of the last index

O(logn)
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        i, j, ll = 0, len(letters)-1, len(letters)

        while i <= j:
            mid = (i+j)/2
            if letters[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return letters[(i)%ll] # just to process the elements to left of 0th index or right of last index

print Solution().nextGreatestLetter(["e", "h", "k"], "l")
