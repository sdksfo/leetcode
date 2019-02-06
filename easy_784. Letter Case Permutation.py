

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
       	if s:
       		rest = self.letterCasePermutation(s[1:])
       		return [s[0].lower() + i for i in rest] + [s[0].upper() + i for i in rest] if s[0].isalpha() else [s[0] + i for i in rest]
       	return ['']

print Solution().letterCasePermutation('12345')
