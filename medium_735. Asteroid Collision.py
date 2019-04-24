"""
Straightforward implementation using stack. There is only collision if prev item in stack faces right and curr item faces left.
a) We add each asterroid into a stack
b) Compare the last elements in the stack and check if its collidable.
c) If so, pop the smallest element.
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)
            while asteroid < 0 and len(stack) >= 2 and stack[-1] < 0 < stack[-2]:
                if abs(stack[-1]) > abs(stack[-2]):
                    stack.pop(-2)
                elif abs(stack[-1]) < abs(stack[-2]):
                    stack.pop(-1)
                else:
                    stack.pop(-1), stack.pop(-1)
        return stack
