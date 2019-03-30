
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A, B = A.split(), B.split()
        A, B= {word: A.count(word) for word in A}, {word: B.count(word) for word in B}

        def getMissing(a, b):
        	return [w for w in a if a[w] < 2 and w not in b]

        return getMissing(A, B) + getMissing(B, A)
