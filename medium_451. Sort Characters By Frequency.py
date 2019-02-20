
""" Idea: Add items with their counts into a heap with count acting as priority. Use negative operand so that the maximum elements comes out first. """

import heapq
from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = defaultdict(int)
        for char in s:
        	counts[char] += 1
        heap = []
        for k, v in counts.items():
        	heapq.heappush(heap, (-v, k))

        str_buff = ''

        while heap:
        	count, char = heapq.heappop(heap)
        	str_buff += char * abs(count)

        return str_buff

print Solution().frequencySort('Aabb')
