
"""Store in heap and pop based on frequency."""

import heapq
from collections import defaultdict


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hashmap = defaultdict(int)
        paragraph = paragraph.replace(",","%").replace(" ","%").replace(".","%").replace("!","%").replace("?","%").replace(";","%").replace("'","%").lower()
        words = filter(lambda x:x , paragraph.split('%'))
        banned = set(banned)
        heap = []

        for word in words:
        	hashmap[word] += 1

        for word, count in hashmap.items():
        	heapq.heappush(heap, (-count, word))

        while heap:
        	count, word = heapq.heappop(heap)
        	if word not in banned:
        		return word

print Solution().mostCommonWord("a.?.", [])
