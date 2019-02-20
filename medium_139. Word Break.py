
# Top down solution

class Solution(object):
    cache = {}
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or s in wordDict:
            return True
        if s not in self.cache:
            self.cache[s] = any([s[:i] in wordDict and self.wordBreak(s[i:], wordDict) for i in xrange(len(s))])
        return self.cache[s]

# Bottom up solution

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        table = [True] + [False for i in range(len(s))]

        for i in xrange(1,len(s)+1):
            for j in xrange(i):
                if table[j] and s[j:i] in wordDict:
                    table[i] = True
        return table[-1]

print Solution().wordBreak("a", ["a"])