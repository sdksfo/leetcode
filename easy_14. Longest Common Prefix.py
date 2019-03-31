
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]: return ''

        i, strs = 0, sorted(strs, key=len)

        while i < len(strs[0]) and len(set([word[i] for word in strs])) == 1:
            i += 1

        return strs[0][:i]

print Solution().longestCommonPrefix(["a"])
