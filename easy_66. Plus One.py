"""
Requirement:

Add 1 to the list and return a new list

Approach:

1) Start with carry as 1
2) Iterate from the reverse direction, as long as there is carry and array is not exhausted
3) Each num in the array = (num[i]+carry)%10
4) New carry = (num[i]+carry)/10
5) If array is exhausted and there is carry return [carry] + [nums]

Complexity:

Time - O(n) Space O(1)

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, i = 1, len(digits)-1

        while carry and i > -1:
        	total = digits[i] + carry
        	digits[i], carry = total%10, total/10
        	i -= 1

        return [carry]+digits if carry else digits

print Solution().plusOne([1,1,8,8,1,2,3])
