"""
Requirement:

Roman to integer conversion

Approach:

1) For each char assign a precedence based on their value. 'I' has value 1 and has lower precedence than 'M' which has value 1000
2) Read the roman string backwards
3) If the precedence of curr char is greater than prev char, add curr_val to running total else subtract curr_val from total.

Complexity:

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def romanToInt(self, s):
		romans, total, prev = {'I': (1, 0), 'V': (5, 1), 'X': (10, 2), 'L': (50, 3), 'C': (100, 4), 'D': (500, 5), 'M': (1000, 6)}, 0, -1

		for i in xrange(len(s)-1, -1, -1):
			curr_val, curr = romans[s[i]]
			total = (total + curr_val) if curr >= prev else (total - curr_val)
			prev = curr

		return total

print Solution().romanToInt('XII')
