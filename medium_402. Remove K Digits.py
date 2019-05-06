# Explanation

# If we remove the greatest MSB at each step, we can get the minimum number
# Iterating from left, for each digit check if the next digit is smaller than it. If so, remove the current digit. e.g 1419 remove '4'
# If none of the digits are removed at a step, remove the last digit e.g 112, remove '2'

# Use a stack data structure to repeatedly remove bigger numbers.

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        return str(int((''.join((stack[:-k] if k else stack) or ['0']))))

print Solution().removeKdigits('1034', 3)
