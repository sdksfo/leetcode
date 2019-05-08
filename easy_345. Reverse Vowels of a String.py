

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s, i, j, vowels = list(s), 0, len(s)-1, set('AEIOUaeiou')

        while i < j:
        	if s[i] not in vowels:
        		i += 1
        	elif s[j] not in vowels:
        		j -= 1
        	elif s[i] in vowels and s[j] in vowels:
        		s[i], s[j] = s[j], s[i]
        		i += 1
        		j -= 1

        return ''.join(s)

print Solution().reverseVowels('leetcode')
