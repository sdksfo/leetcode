"""
Requirement:

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Approach:

1) Use two pointer placed at both ends of string
2) If both pointers are at valid chars, check if chars match
3) Increment i or decrement j if they are not at valid chars.

Complexity:

Time: O(n)
Space: O(1)
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = set('0123456789abcdefghijklmnopqrstuvwxyz')

        i, j = 0, len(s) - 1

        while i <= j:
        	a, b = s[i].lower(), s[j].lower()
        	if a in chars and b in chars:
        		if a != b: return False
        		i += 1
        		j -= 1
        	elif a not in chars:
        		i += 1
        	elif b not in chars:
        		j -= 1
        return True
