
"""
Construct a palindrome with every character that occurs more than twice.

ccdefccd -> Here c occurs 4 times and d occurs 2 times and hence we can
form with cc,cc and d,d on either side for the palindrome
"""

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        palin, single, hashmap = '', '', defaultdict(int)

        for char in s:
            hashmap[char] += 1

        for char, count in hashmap.items():
            if count/2:
                palin = ((count/2)*char) + palin + ((count/2)*char)
            if count%2:
                single = char

        if single:
            palin = palin[:len(palin)/2] + single + palin[(len(palin))/2:]

        return len(palin)

print Solution().longestPalindrome('cccdd')
