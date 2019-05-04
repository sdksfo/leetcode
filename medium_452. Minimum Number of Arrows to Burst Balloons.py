
# Approach 1: Merge as many intervals as possible and return length of stack

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points)

        stack = []

        for point in points:
            if not stack:
                stack.append(point)
            else:
                (old_start, old_end), (new_start, new_end) = stack[-1], point
                if old_start <= new_start <= old_end:
                    stack[-1] = [max(old_start, new_start), min(old_end, new_end)]
                else:
                    stack.append(point)

        return len(stack), stack

print Solution().findMinArrowShots([[12,16], [2,8], [1,8], [7,12]])

# Appraoch 2: We avoid using a stack. We sort based on ending times. The number of non-overlapping intervals is the number
# of arrows needed

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points, end, arrows = sorted(points, key = lambda x: x[1]), -float('inf'), 0

        for point in points:
            if point[0] > end:
                arrows += 1
                end = point[1]

        return arrows
