"""Create a stack and whenever a white space is encountered pop from stack and add to the buff"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output, buff = '', []

        for char in s:
            if char == ' ':
                while buff:
                    output += buff.pop()
                output += char
            else:
                buff.append(char)

        while buff:
            output += buff.pop()

        return output

print Solution().reverseWords("Let's   take LeetCode contest ")
