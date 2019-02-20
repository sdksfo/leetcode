
"""Build a heap of elements and their occurences. Pop until the count is reached"""

import heapq

from collections import defaultdict

class Solution(object):
    def heapify(self, nums):
        """Adds elements and their counts to a heap"""
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        heap = []
        for num, total in counts.items():
            heapq.heappush(heap, (-total, num)) # negative operand so that highest becomes lowest and gets fetched first
        return heap

    def topKFrequent(self, nums, k):
        if nums:
            elements_heap = self.heapify(nums)
            return [heapq.heappop(elements_heap)[1] for i in xrange(k)]
        return []

print Solution().topKFrequent([], 2)
