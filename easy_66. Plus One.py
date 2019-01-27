


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        for i in xrange(len(digits)-1, -1, -1):
        	digits[i], c = (digits[i]+c) % 10, (digits[i]+c) / 10
        if c:
        	digits.insert(0, c)
        return digits

print Solution().plusOne([0])
