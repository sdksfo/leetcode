

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combo(ints, k):
            if k == 0:
                return [[]]
            output, int_len = [], len(ints)
            for i in xrange(int_len):
                if (int_len - i) < k: return output
                output.extend([[ints[i]]+j for j in combo(ints[i+1:], k-1)])
            return output
        return combo(range(1, n+1), k)

print Solution().combine(5, 3)
