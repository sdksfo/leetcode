"""
Traverse backwards and maintain a stack for last seen highest temperature. This barely passes LC test cases and is sub-optimal. Will try this again with a different approach.
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack, output = [], [0 for _ in T]

        for i in xrange(len(T)-1, -1, -1):
            curr = T[i]
            while stack and curr >= T[stack[-1]]:
                stack.pop()
            if stack: output[i] = stack[-1] - i
            stack.append(i)

        return output

print Solution().dailyTemperatures([71,71,76,71,71,76,71,71,71])
