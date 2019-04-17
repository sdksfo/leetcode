"""
Requirement:

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Approach:

Use a hashmap to store the indexes and also capture minimum distance at each step

Complexity:

Time: O(n) Space: O(1)
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hashmap, distance = {word1: float('INF'), word2: float('INF')}, len(words)

        for i, word in enumerate(words):
        	if word == word1 or word == word2:
        		hashmap[word] = i
        		distance = min(mini, abs(hashmap[word1] - hashmap[word2]))

        return distance
