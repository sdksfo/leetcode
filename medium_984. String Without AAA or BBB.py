"""
Requirement:

Write no more than 2 a's or b's together

Approach:

a) The rules for writing is as below:

    a) We can write each character once or twice
    b) If one character is larger than the other character, write twice, else just once

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def strWithout3a3b(self, A, B):
        ans, writeA = [], False

        while A or B:
            if len(ans) > 1 and ans[-1] == ans[-2]: # change when character count is 2
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B # write whichever character is more

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return ''.join(ans)

print Solution().strWithout3a3b(4,1)
