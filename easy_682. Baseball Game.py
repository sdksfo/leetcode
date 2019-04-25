

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = [0, 0]

        for op in ops:
        	if op == '+':
        		stack.append(stack[-1]+stack[-2])
        	elif op == 'C':
        		stack.pop()
        	elif op == 'D':
        		stack.append(stack[-1]*2)
        	else:
        		stack.append(int(op))

        return sum(stack)

print Solution().calPoints(["5","-2","4","C","D","9","+","+"])
