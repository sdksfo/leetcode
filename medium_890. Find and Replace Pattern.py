
"""
Create a mapping of char seen to char in pattern and use information to decide identify words
"""

class Solution(object):

    def isValid(self, word, pattern):
        """checks if the word follows the pattern"""
        if len(word) != len(pattern):
            return False

        hashmap, assigned = {}, set()

        for i in xrange(len(word)):
            if word[i] not in hashmap and pattern[i] in assigned:
                return False
            if word[i] in hashmap and hashmap[word[i]] != pattern[i]:
                return False
            assigned.add(pattern[i])
            hashmap[word[i]] = pattern[i]
        return True

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        return [word for word in words if self.isValid(word, pattern)]

print Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")
