
# Greedily start filling from the most frequently occuring character to the least occuring character.

import heapq
import collections

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        chars = map(lambda x: [-x[1],x[0]], collections.Counter(S).items())

        heapq.heapify(chars)

        if any([abs(x[0]) > (len(S)+1)/2 for x in chars]):
            return ''

        output = []

        while len(chars) >= 2:
        	count_a, char_a = heapq.heappop(chars)
        	count_b, char_b = heapq.heappop(chars)
        	output.extend([char_a, char_b])
        	if count_a < -1:
                heapq.heappush(chars, [count_a+1, char_a])
        	if count_b < -1:
                heapq.heappush(chars, [count_b+1, char_b])

        return ''.join(output) if not chars else ''.join(output)+chars[0][1]
