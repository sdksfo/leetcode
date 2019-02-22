"""If extra space is allowed, use a hashmap to store the count of characters else sort and use two pointer"""

from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        hashmap = defaultdict(int)
        for char in s: hashmap[char] += 1
        for char in t:
        	if char not in hashmap: return False
        	hashmap[char] -= 1
        return all([v==0 for k,v in hashmap.items()])

print Solution().isAnagram('anagram', 'nnnnnnn')
