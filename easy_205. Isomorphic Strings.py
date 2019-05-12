class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        
        stot, ttos = {}, {}

        for i in xrange(len(s)):
        	if s[i] in stot and t[i] in ttos:
        		if stot[s[i]] != t[i] or ttos[t[i]] == s[i]:
        			return False
        	elif s[i] not in stot and t[i] not in ttos:
        		stot[s[i]], ttos[t[i]] = t[i], s[i]
        	else:
        		return False

        return True
