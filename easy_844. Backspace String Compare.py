

# Approach 1: Using a stack

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def parse(string):
            stack = []
            for c in string:
                if c == '#':
                    stack.pop() if stack else None
                else:
                    stack.append(c)
            return ''.join(stack)
        return parse(S) == parse(T)

# Approach 2: Using constant space

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i , j, i_ctr, j_ctr = len(S) - 1, len(T) - 1, 0, 0

        while i > -1 or j > -1:
            while i > -1 and (S[i] == '#' or i_ctr):
                i_ctr = i_ctr + 1 if S[i] == '#' else i_ctr - 1
                i -= 1
            while j > -1 and (T[j] == '#' or j_ctr):
                j_ctr = j_ctr + 1 if T[j] == '#' else j_ctr - 1
                j -= 1
            if (i > -1 and j > -1 and S[i] != T[j]) or (i < 0 and j > -1) or (j < 0 and i > -1):
                return False
            i -= 1
            j -= 1

        return True

print Solution().backspaceCompare("a#abcd", "a#abc#cd")
