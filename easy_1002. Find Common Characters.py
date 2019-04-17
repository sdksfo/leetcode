"""
Requirement:

Return all characters that show up in the array

Approach:

a) Create a char_count dict that has all the chars in word 1 and its counts
b) Update the char_counts hashmap by looking up other words in the list

Complexity:

Time: O(m*n), where m is length of list and n is number of chars in each word
Space: O(n)
"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
    	char_count = {char:A[0].count(char) for char in A[0]} if A else {}
    	for word in A[1:]:
    		for char in char_count:
    			char_count[char] = min(char_count[char], word.count(char))
    	output = [d*v for d,v in char_count.items() if v]

        return list(''.join(output))

print Solution().commonChars(["bella","label","roller"])
