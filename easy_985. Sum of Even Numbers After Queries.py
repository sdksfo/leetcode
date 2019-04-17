

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        output = []

        curr_sum = sum(i for i in A if i%2 == 0)

        for val, index in queries:
            prev, curr = A[index], A[index] + val
            A[index] = curr
            if curr % 2 == 0:
                curr_sum += curr if prev%2 else curr-prev
            else:
                curr_sum -= prev if not prev%2 else 0
            output.append(curr_sum)

        return output

print Solution().sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]])
