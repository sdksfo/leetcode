
"""
Iterate from the back and keep adding to the output list until the count is reached
"""


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ctr, output, buff = 0, [], ''

        for i in xrange(len(S)-1, -1, -1) :
        	if S[i] != '-':
        		buff = S[i].upper() + buff
        		ctr += 1
        	if ctr == K:
        		output.insert(0, buff)
        		buff, ctr = '', 0
        if buff:
        	output.insert(0, buff)

        return '-'.join(output)

print Solution().licenseKeyFormatting("--------EyRfCyHxyUJzhygiazYpjuDFdHvrnDwoQKQEsccLDiwhpmjueADIzqIvExbDDFnEGovAxYeszbzuTekRuWUPXRPbVKJuDQzIzzTj", 16)
