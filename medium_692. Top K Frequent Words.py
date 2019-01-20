# Explanation

# Create a hashmap of words and count
# Add the elements from hashmap into a priority queue with frequency as priority and weight (lowest alphabet gets most weight, so that it can be retrieved first)
# pop the 'k' words from pq

import heapq, collections

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        heap, hashmap = [], collections.defaultdict(int)
        for word in words:
        	hashmap[word] += 1
        weight = len(hashmap)
        for f, w in sorted([(f,w) for w,f in hashmap.items()]):
        	heapq.heappush(heap, [f, weight, w])
        	weight -= 1
        return [w for (f, wt, w) in heapq.nlargest(k, heap)]

print Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
