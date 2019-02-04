

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output, bfr = [], ''
        for i in xrange(len(s)-1, -1, -1):
            if s[i] != ' ':
                bfr += s[i]
            elif bfr:
                output.append(bfr[::-1])
                bfr = ''
        output.append(bfr[::-1]) if bfr else None
        return ' '.join(output)

print Solution().reverseWords("sky is blue")
