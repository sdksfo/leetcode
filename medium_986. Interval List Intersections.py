
# Approach 1: Straightforward intersection calculation

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j, output = 0, 0, []

        while i < len(A) and j < len(B):
            start_a, end_a = A[i]
            start_b, end_b = B[j]

            if start_a <= start_b <= end_a:
                output.append([start_b, min(end_a, end_b)])
            elif start_b <= start_a <= end_b:
                output.append([start_a, min(end_a, end_b)])

            i = i+1 if end_a <= end_b else i
            j = j+1 if end_b <= end_a else j

        return output

print Solution().intervalIntersection([[1,2],[3,4],[5,9],[19,20],[39,60]], [[1,5]])
