


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        l, found, start, output = 0, False, None, ''

        for i in xrange(len(S)):
        	if S[i] == '(':
        		if not found:
        			found, start = True, i
        		l -= 1
        	elif S[i] == ')':
        		l += 1
        		if l == 0:
        			output += S[start+1:i]
        			found = False
        return output

print Solution().removeOuterParentheses("(())")
