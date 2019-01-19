
# Solution 1: Using cancellation technique

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x_axis = y_axis = 0
        for move in moves:
        	if move == 'L': x_axis -= 1
        	if move == 'R': x_axis += 1
        	if move == 'U': y_axis += 1
        	if move == 'D': y_axis -= 1
        return x_axis == y_axis == 0

# Solution 2: Using python's inbuilt - faster as there is a short circuit

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

print Solution().judgeCircle('LLR')
