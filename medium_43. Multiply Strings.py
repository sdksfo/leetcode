


class Solution(object):
    def getPart(self, n1, n2, carry=0):
        if not n2: return str(carry)
        curr = int(n1) * int(n2[-1]) + carry
        carry, curr = curr/10, curr%10
        return self.getPart(n1, n2[:-1], carry) + str(curr)

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tens, total = 0, 0

        for i in xrange(len(num2)-1, -1, -1):
            total += int(self.getPart(num2[i], num1)) * (10 ** tens)
            tens += 1
        return str(total)

print Solution().multiply('123', '4568')
