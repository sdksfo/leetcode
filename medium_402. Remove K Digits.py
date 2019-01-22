# Explanation

# If we remove the greatest MSB at each step, we can get the minimum number
# Iterating from left, for each digit check if the next digit is smaller than it. If so, remove the current digit. e.g 1419 remove '4'
# If none of the digits are removed at a step, remove the last digit e.g 112, remove '2'

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for i in xrange(k):
            for j in xrange(len(num)-1):
                if num[j] > num[j+1]:
                    num = num[:j]+num[j+1:]
                    break
            else:
                num = num[:-1]
        return str(int(num)) if num else '0'

print Solution().removeKdigits('1433219', 2)
