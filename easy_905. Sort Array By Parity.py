"""
Requirement:

a) Given an array modify in place to return an output with even elements followed by odd

Approach 1:

Algorithm:

a) Keep the even-pointer at idx 0
b) Iterate through the array, if even number is encountered, swap the element at index 'i' with element at even-pointer and increment even-pointer
c) If odd number is encountered, do nothing

Approach 2:

Algorithm:

a) Use a modified DNF flag approach using odd and even indixes, with even idx on left most element and odd at right most element
b) Iterate until even-pointer < odd-pointer
c) If even-pointer points to odd element and odd-pointer points at even element, swap both and increment and decrement odd and even pointers respectively.
d) If even-pointer points to even element, only increment even pointer and likewise decrement odd pointer if its at odd element.

Complexity:

Time: O(n)
Space: O(1)

"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_idx =  i = 0

        while i < len(A):
            if A[i] % 2 == 0:
                A[i], A[even_idx] = A[even_idx], A[i]
                even_idx += 1
            i += 1

        return A

print Solution().sortArrayByParity([0,32,1,4,6])

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_idx, odd_idx = 0, len(A) - 1

        while even_idx < odd_idx:
            if not A[even_idx] % 2:
                even_idx += 1
            elif A[odd_idx] % 2:
                odd_idx -= 1
            else:
                A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
                even_idx += 1
                odd_idx -= 1
        return A

print Solution().sortArrayByParity([0,5,32,1,4,6,4,3])
