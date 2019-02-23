

from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1

        for idx, char in enumerate(s):
            if hashmap[char] == 1:
                return idx
        return -1
