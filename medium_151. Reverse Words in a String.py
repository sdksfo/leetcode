"""
Requirement:

Given an input string, reverse the string word by word.

Approach:

1) Split string into list of words
2) Return the reversed data separated by space

Complexity:

Time - O(n), Space - O(n)

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(filter(lambda x: x, s.split(' '))[::-1])

print Solution().reverseWords("a good   example")
