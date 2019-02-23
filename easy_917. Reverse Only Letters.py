

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i, j, s = 0, len(S) - 1, list(S)

        while i < j:
        	if s[i].isalpha() and s[j].isalpha():
        		s[i], s[j] = s[j], s[i]
        		i += 1
        		j -= 1
        	elif s[j].isalpha():
        		i += 1
        	elif s[i].isalpha():
        		j -= 1
        	else:
        		i += 1
        		j -= 1
        return ''.join(s)

print Solution().reverseOnlyLetters("8_28")

