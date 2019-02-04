
"""
25525511135 -> could be split into length of 1,2 and 3

1) only 1 digit number can be 0
2) numbers must be in range 0 - 255
3) max_length of string should be in range string_len/dot_count ie 3 * (dot_count + 1) = 12

Break it down into 1 byte, 2 byte and 3 byte strings and recursively compute based on number of chars left or dots left
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def break_ip(s, dots):
        	if dots == 0:
        		return [] if (len(s) > 3 or not s or int(s) > 255 or (s[0] == '0' and len(s) > 1)) else [s]
        	one_byte = break_ip(s[1:], dots-1)
        	two_byte = break_ip(s[2:], dots-1) if (s and s[0] != '0') else []
        	three_byte = break_ip(s[3:], dots-1) if (s and s[0] != '0' and int(s[:3]) < 256) else []
        	total = [one_byte, two_byte, three_byte]
        	return filter(lambda x: x.count('.') == dots, [s[:i+1] + '.' + j for i in xrange(len(total)) for j in total[i]])
        return break_ip(s, 3)

print Solution().restoreIpAddresses('111')