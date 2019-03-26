
# if there is anything other than 1,6,8,9 it will not look right

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        output = ''

        for n in num:
        	if n == '6':
        		output += '9'
        	elif n == '9':
        		output += '6'
        	elif n in ('081'):
        		output += n
        	else:
        		return False

        return output == num[::-1]

print Solution().isStrobogrammatic('1908061')
