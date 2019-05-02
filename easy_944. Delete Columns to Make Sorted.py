


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        output = 0

        for i in xrange(len(A[0]) if A else 0):
        	prev = ''
        	for word in A:
        		if prev and word[i] < prev[i]:
        			output += 1
        			break
        		prev = word

        return output

print Solution().minDeletionSize(["zyx","wvu","tsr"])
