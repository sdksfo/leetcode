

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capitals = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        capital_count, small_count = 0, 0

        for char in word:
        	if char in capitals:
        		if small_count: return False
        		capital_count += 1
        	else:
        		if capital_count > 1: return False
        		small_count += 1
        return True

print Solution().detectCapitalUse('Flag')
