

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum((i in set(J) for i in S))

print Solution().numJewelsInStones('aA', 'aAAbbbb')
