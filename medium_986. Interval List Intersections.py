

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]

# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Use two pointer technique

# a) If start is between the two, then add it to the intersection
# b) If start is greater than the end, increase one of the indices

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        def intersect(C, D):
        	return C.start <= D.start <= C.end or D.end == C.start

        i, j, output = 0, 0, []

        while i < len(A) and j < len(B):
        	if intersect(A[i], B[j]) or intersect(B[j], A[i]):
        		output.append(Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end)))
        	if (B[j].end < A[i].start) or (B[j].end < A[i].end):
        		j += 1
        	else:
        		i += 1
        return output

A = [[8,15]]
B= [[2,6],[8,10],[12,20]]

solns =  Solution().intervalIntersection([Interval(*i) for i in A], [Interval(*i) for i in B])

for i in solns:
	print i.start, i.end
