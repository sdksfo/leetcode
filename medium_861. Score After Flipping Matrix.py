
# For rows - if it starts with 0 flip
# For cols - start with MSB and check for each col, if flipping will increase the total or not

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        curr = 0
        for i, d in enumerate(A):
        	if d[0] == 0:
        		A[i] = [1-j for j in d]
        	curr += int(''.join([str(j) for j in A[i]]), 2)

        for i in xrange(1, len(A[0])):
        	for j in xrange(len(A)):
        		A[j][i] = 1 - A[j][i]
        	total = sum(int(''.join([str(j) for j in i]), 2) for i in A)
        	if total < curr:
        		for j in xrange(len(A)):
        			A[j][i] = 1 - A[j][i]
        	curr = max(total, curr)
        return curr

print Solution().matrixScore([[0,0,1,1,1,1,1,1,0],[1,0,1,0,0,1,0,1,0],[1,1,0,0,0,0,0,1,1]])
