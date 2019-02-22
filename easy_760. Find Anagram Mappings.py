

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        hashmapA = {i:A[i] for i in xrange(len(A))}
        hashmapB = {B[i]:i for i in xrange(len(B))}

        return [hashmapB[hashmapA[i]] for i in xrange(len(A))]

print Solution().anagramMappings([1,2], [2,1])
