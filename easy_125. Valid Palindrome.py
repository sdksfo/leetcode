

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ''.join([i.lower() for i in s if i.isalnum()])
        return temp == temp[::-1]

print Solution().isPalindrome("A man, a plan, a canal: Panamaa")
