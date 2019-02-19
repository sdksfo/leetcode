
"""
Sort the input dictionary in the order of their lengths and then iterate through the
source string looking for the string.
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d, key=lambda x: x.lower())
        output = ''
        for word in d:
        	if len(s) >= len(word):
	        	i = j = 0
	        	while i < len(word) and j < len(s):
	        		if word[i] == s[j]:
	        			i += 1
	        		j += 1
	        	if i == len(word) and len(output) < i:
	        		output = word
        return output

print Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
