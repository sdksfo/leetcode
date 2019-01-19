
# Solution 1: Modifying the input matrix

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        while A and A[0]:
        	output.append([inner.pop(0) for inner in A])
        return output

# Solution 2: Without modifying the input matrix

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]:
        	return A

        return [[A[j][i] for j in xrange(len(A))] for i in xrange(len(A[0]))]

print Solution().transpose([[1,2,3],[4,5,6],[7,8,9]])
